select 
	names.name_first as first_name,
    names.name_last as last_name,
    location.location_state as state,
    age.dob_age as age, 
    contact.cell as cell,
    picture.picture_large as picture
 from users_data.names
 	join users_data.location on users_data.names.id_value = users_data.location.id_value
    join users_data.age on users_data.age.id_value = users_data.names.id_value
    join users_data.contact on users_data.names.id_value = users_data.contact.id_value
    join users_data.picture on users_data.names.id_value = users_data.picture.id_value
order by age
limit 10;