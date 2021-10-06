create external table users_data.names(
    id_name varchar(32),
    id_value varchar(64),
    gender varchar(16),
    name_title varchar(32),
    name_first varchar(64),
    name_last varchar(64)
 )
 ROW FORMAT SERDE
    'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://users-data-605645534020';


create external table users_data.picture(
   id_name varchar(32),
   id_value varchar(32),
   picture_large varchar(64),
   picture_medium varchar(64),
   picture_thumbnail varchar(64)
)
ROW FORMAT SERDE
   'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://users-data-605645534020';

create external table users_data.location(
   id_name varchar(32),
   id_value varchar(32),
   location_street_number int,
   location_street_name varchar(64),
   location_city varchar(32),
   location_state varchar(32),
   location_country varchar(32),
   location_postcode varchar(32),
   location_coordinates_latitude varchar(64),
   location_coordinates_longitude varchar(64),
   location_timezone_offset varchar(32),
   location_timezone_description varchar(32),
   nat varchar(16)
)
ROW FORMAT SERDE
   'org.openx.data.jsonserde.JsonSerDe'
 LOCATION 's3://users-data-605645534020';

 create external table users_data.age(
   id_name varchar(32),
   id_value varchar(32),
   dob_date varchar(32),
   dob_age int,
   registered_date varchar(32),
   registered_age int
)
ROW FORMAT SERDE
   'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://users-data-605645534020';

create external table users_data.contact(
  id_name varchar(32),
  id_value varchar(32),
  email varchar(32),
  phone varchar(32),
  cell varchar(32)
)
ROW FORMAT SERDE
  'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://users-data-605645534020';
