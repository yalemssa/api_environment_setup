select DISTINCT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri
	, ao3.display_string as parent_parent_display_string
	, ao2.display_string as parent_display_string
	, ao.display_string as display_string
	, CONCAT('/repositories/', tc.repo_id, '/top_containers/', tc.id) as tc_uri
	, ev2.value as tc_type
	, tc.indicator as tc_indicator
from archival_object ao
left join archival_object ao2 on ao2.id = ao.parent_id
left join archival_object ao3 on ao3.id = ao2.parent_id
left join instance on instance.archival_object_id = ao.id
left join sub_container sc on sc.instance_id = instance.id
left join top_container_link_rlshp tclr on tclr.sub_container_id = sc.id
left join top_container tc on tclr.top_container_id = tc.id
LEFT JOIN enumeration_value ev2 on ev2.id = tc.type_id
where ao.root_record_id = 4869
and (ao.parent_id = 2012449 or ao2.parent_id = 2012461)
and tc.id is not null
ORDER BY CAST(tc.indicator AS UNSIGNED)