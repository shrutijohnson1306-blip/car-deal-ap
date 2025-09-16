from django.shortcuts import render
from django.db import connection

def run_query(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    return [dict(zip(columns, row)) for row in rows]

def customers_by_state(request):
    data = run_query("""
        SELECT c.state, COUNT(DISTINCT o.customer_id) AS total_customers
        FROM order_t o
        JOIN customer_t c ON o.customer_id = c.customer_id
        GROUP BY c.state
        ORDER BY total_customers DESC;
    """)
    return render(request, "analytics/customers_by_state.html", {"data": data})

def top_vehicle_makers(request):
    data = run_query("""
        SELECT p.vehicle_maker, COUNT(o.order_id) AS total_orders
        FROM order_t o
        JOIN product_t p ON o.product_id = p.product_id
        GROUP BY p.vehicle_maker
        ORDER BY total_orders DESC
        LIMIT 5;
    """)
    return render(request, "analytics/top_vehicle_makers.html", {"data": data})

def preferred_maker_by_state(request):
    data = run_query("""
        SELECT c.state, p.vehicle_maker, COUNT(*) AS total_orders
        FROM order_t o
        JOIN product_t p ON o.product_id = p.product_id
        JOIN customer_t c ON o.customer_id = c.customer_id
        GROUP BY c.state, p.vehicle_maker
        ORDER BY c.state, total_orders DESC;
    """)
    return render(request, "analytics/preferred_maker_by_state.html", {"data": data})

def avg_rating_by_quarter(request):
    data = run_query("""
        SELECT 
            quarter_number,
            AVG(
                CASE customer_feedback
                    WHEN 'Excellent' THEN 5
                    WHEN 'Good' THEN 4
                    WHEN 'Average' THEN 3
                    WHEN 'Poor' THEN 2
                    WHEN 'Very Poor' THEN 1
                END
            ) AS avg_rating
        FROM order_t
        GROUP BY quarter_number
        ORDER BY quarter_number;
    """)
    return render(request, "analytics/avg_rating_by_quarter.html", {"results": data})


def feedback_distribution(request):
    data = run_query("""
        SELECT customer_feedback, COUNT(*) * 100.0 / SUM(COUNT(*)) OVER() AS percentage
        FROM order_t
        GROUP BY customer_feedback;
    """)
    return render(request, "analytics/feedback_distribution.html", {"data": data})

def orders_by_quarter(request):
    data = run_query("""
        SELECT quarter_number, COUNT(*) AS total_orders
        FROM order_t
        GROUP BY quarter_number
        ORDER BY quarter_number;
    """)
    return render(request, "analytics/orders_by_quarter.html", {"data": data})

def revenue_change(request):
    data = run_query("""
        WITH revenue_data AS (
            SELECT quarter_number,
                   SUM(quantity * (vehicle_price - (vehicle_price * discount / 100))) AS net_revenue
            FROM order_t
            GROUP BY quarter_number
        )
        SELECT quarter_number,
               net_revenue,
               ROUND(((net_revenue - LAG(net_revenue) OVER (ORDER BY quarter_number)) 
                     / LAG(net_revenue) OVER (ORDER BY quarter_number) * 100),2) AS pct_change
        FROM revenue_data;
    """)
    return render(request, "analytics/revenue_change.html", {"data": data})

def revenue_orders_trend(request):
    data = run_query("""
        SELECT quarter_number,
               COUNT(order_id) AS total_orders,
               SUM(quantity * (vehicle_price - (vehicle_price * discount / 100))) AS net_revenue
        FROM order_t
        GROUP BY quarter_number
        ORDER BY quarter_number;
    """)
    return render(request, "analytics/revenue_orders_trend.html", {"data": data})

def avg_discount_by_card(request):
    data = run_query("""
        SELECT c.credit_card_type, AVG(o.discount) AS avg_discount
        FROM order_t o
        JOIN customer_t c ON o.customer_id = c.customer_id
        GROUP BY c.credit_card_type;
    """)
    return render(request, "analytics/avg_discount_by_card.html", {"data": data})

def shipping_time(request):
    data = run_query("""
        SELECT quarter_number, AVG(ship_date - order_date) AS avg_shipping_days
        FROM order_t
        GROUP BY quarter_number
        ORDER BY quarter_number;
    """)
    return render(request, "analytics/shipping_time.html", {"data": data})

