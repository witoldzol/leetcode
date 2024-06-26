-- https://leetcode.com/problems/average-time-of-process-per-machine/description/

-- notice the cast to numeric value inside the round function
select a.machine_id,
round(avg((b.timestamp - a.timestamp)::numeric), 3) as processing_time from Activity a
join Activity b on a.machine_id = b.machine_id 
and a.process_id = b.process_id
and a.activity_type = 'start'
and b.activity_type = 'end'
group by a.machine_id

-- instead of casting lets use a function
create or replace function round_avg(value numeric, decimal_places integer)
returns numeric as $$
begin
    return round(value, decimal_places);
end;
$$ language plpgsql;

select a.machine_id,
round_avg((b.timestamp - a.timestamp), 3) as processing_time 
from Activity a
join Activity b on a.machine_id = b.machine_id 
and a.process_id = b.process_id
and a.activity_type = 'start'
and b.activity_type = 'end'
group by a.machine_id

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start = activity.query('activity_type == "start"')
    end = activity.query('activity_type == "end"')
    merge_df = pd.merge(start, end, on=['machine_id', 'process_id'], suffixes=['_start', '_end'])
    merge_df['processing_time'] = merge_df['timestamp_end'] - merge_df['timestamp_start']
    return merge_df.groupby(['machine_id'])['processing_time'].mean().round(3).reset_index()
    
