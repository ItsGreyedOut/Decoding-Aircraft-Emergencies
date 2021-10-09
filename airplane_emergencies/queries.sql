--Squawk Code Count
select distinct ft.squawk, count(distinct fs.flight_id)
from flight_summary fs, flight_trajectory ft, aircraft_metadata am
where fs.icao24 = ft.icao24
and am.icao24 = ft.icao24
--and ft.squawk = 7700
group by ft.squawk
order by count(distinct fs.flight_id) DESC
****************************************************
--Tweet Problem Count
select distinct fs.tweet_problem, count(distinct fs.flight_id)
from flight_summary fs, flight_trajectory ft, aircraft_metadata am
where fs.icao24 = ft.icao24
and am.icao24 = ft.icao24
--and ft.squawk = 7700
group by fs.tweet_problem

******************************************
select distinct fs.avh_problem, count(distinct fs.flight_id)
from flight_summary fs, flight_trajectory ft, aircraft_metadata am
where fs.icao24 = ft.icao24
and am.icao24 = ft.icao24
--and ft.squawk = 7700
group by fs.avh_problem
*************************************
--result count
select distinct fs.tweet_result, count(distinct fs.flight_id)
from flight_summary fs, flight_trajectory ft, aircraft_metadata am
where fs.icao24 = ft.icao24
and am.icao24 = ft.icao24
--and ft.squawk = 7700
group by fs.tweet_result
***********************************************
--Manufacturer count
select distinct substr(am.manufacturername,1,6), fs.tweet_result, count(distinct fs.flight_id)
from flight_summary fs, flight_trajectory ft, aircraft_metadata am
where fs.icao24 = ft.icao24
and am.icao24 = ft.icao24
--and ft.squawk = 7700
group by substr(am.manufacturername,1,6),fs.tweet_result