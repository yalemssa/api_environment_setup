SELECT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri
	, TRIM(LEADING '/' from CONCAT(IFNULL(ao3.display_string, ''), '/', ao2.display_string)) as parent_title
	, ao.display_string as title
	, ev2.value as container_type
	, tc.indicator as box_num
	, ev3.value as sub_container_type
	, sc.indicator_2 as folder_num
	, NULL as new_folder_num
FROM archival_object ao
JOIN instance on instance.archival_object_id = ao.id
LEFT JOIN sub_container sc on sc.instance_id = instance.id
LEFT JOIN top_container_link_rlshp tclr on tclr.sub_container_id = sc.id
LEFT JOIN top_container tc on tc.id = tclr.top_container_id
LEFT JOIN enumeration_value ev on ev.id = instance.instance_type_id
LEFT JOIN archival_object ao2 on ao2.id = ao.parent_id
LEFT JOIN archival_object ao3 on ao3.id = ao2.parent_id
LEFT JOIN enumeration_value ev2 on ev2.id = tc.type_id
LEFT JOIN enumeration_value ev3 on ev3.id = sc.type_2_id
# limit to a resource
WHERE ao.root_record_id = 2623
# limit to a particular series - this assumes just 2 levels of nesting
AND (ao2.id = 815180 or ao3.id = 815180)
# exclude digital object instances
AND ev.value not like '%digital_object%'
ORDER BY ao.id