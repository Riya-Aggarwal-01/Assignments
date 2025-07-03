Query-1 : select s.customer_id, sum(m.price) as amount_sent
         from sales s
         join menu m on m.product_id=s.product_id
         group by customer_id;


Query-2 : select s.customer_id, count(distinct order_date) as total_days
         from sales s
         group by s.customer_id;

Query-3 : select s.customer_id, s.product_id, m.product_name, s.order_date
          from sales s
          join menu m on s.product_id = m.product_id
          where s.order_date = (
          select min(s2.order_date)
          from sales s2
          where s2.customer_id = s.customer_id
          );

Query 4 : select customer_id,product_id, count(*) as total_times_ordered
          from sales 
          where product_id = 
          (
          select product_id
          from (
          select product_id, count(*) as total_orders
          from sales
          group by product_id
          )
          where total_orders = ( select max(total_order)
          from(
          select product_id,count(*) as total_order
          from sales
          group by product_id
          )))
          group by customer_id,product_id


Query 5 : select customer_id, product_id,count(*) as total_order
          from sales s1
          where (
          select count (*)
          from sales s2
          where s2.product_id=s1.product_id and s1.customer_id=s2.customer_id)
          = (
          select max(order_count)
          from (
          select s3.product_id, COUNT(*) as order_count
          from sales s3
          where s3.customer_id = s1.customer_id
          group by s3.product_id
          ))
	  group by customer_id,product_id

Query 6 : select s.customer_id,s.product_id,s.order_date
          from sales s 
          join members m on m.customer_id=s.customer_id
          where s.order_date = (
          select min(s2.order_date)
          from sales s2 
          where s.customer_id=s2.customer_id and s2.order_Date>=m.join_date
          )

Query 7 : select s.customer_id,s.product_id,s.order_date
          from sales s 
          join members m on m.customer_id=s.customer_id
          where s.order_date = (
          select max(s2.order_date)
          from sales s2 
          where s.customer_id=s2.customer_id and s2.order_Date<m.join_date
          )

Query 8 : select s.customer_id,
          count(*) as total_items,
          sum(m.price) as total_spent
          from sales s
          join menu m on s.product_id = m.product_id
          join members mem on s.customer_id = mem.customer_id
          where s.order_date < mem.join_date
          group by s.customer_id;

Query 9 : select s.customer_id,
          sum(
              case
                 when m.product_name = 'sushi' then m.price * 10 * 2
                 else m.price * 10
              end
           ) as total_points
         from sales s
         join menu m on s.product_id = m.product_id
         group by s.customer_id;

Query 10 : 