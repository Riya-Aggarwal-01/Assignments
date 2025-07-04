Query 1 : select count(distinct user_id) as total_user
        from users

Query 2 : select user_id,count(distinct cookie_id) as total_cookies
          from users
          group by user_id

Query 3 : select count(distinct visit_id)
          from events
          group by EXTRACT(Month from event_time)

Query 4 : select event_type,count(event_type)
          from events
          group by event_type

Query 5 :  select (
           select count(visit_id)
           from events
           where event_type = ( select event_type
           from event_identifier
           where event_name = 'Purchase'
           ))* 100 /
           (select count(visit_id)
           from events) as percentage

Query 6 :
Query 7 :
Query 8 :
Query 9 :