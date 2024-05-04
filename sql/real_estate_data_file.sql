use real_estate_proj;

create table agents (
	agent_id integer auto_increment primary key,
    first_name varchar(50),
    last_name varchar(50),
    address_line_1 varchar(90),
    address_line_2 varchar(50),
    city varchar(30),
    state varchar(2),
    zip varchar(5),
    phone varchar(15),
    start_date date,
    created_at timestamp
);
    
create table properties (
	property_id integer auto_increment primary key,
    address_line_1 varchar(90) NOT NULL,
    address_line_2 varchar(50),
    city varchar(30),
	state varchar(2),
    zip varchar(5) NOT NULL,
    original_listing_price integer,
    sold_price integer,
    type varchar(20),
    sqft integer,
    bedrooms integer,
    bathrooms integer,
    year_built integer,
    on_market date,
    off_market date,
    agent_id integer,
    sold boolean,
    created_at timestamp,
    constraint prop_agent_fk
		foreign key (agent_id)
        references agents (agent_id)
        on delete cascade
		on update restrict,
	constraint check_year check (year_built >= 1600),
    constraint check_type check(lower(type) in ('single family home', 'commercial', 'land', 'multi family home', 'apartment', 'townhouse', 'condo'))
);
    
create table clients (
	client_id integer auto_increment primary key,
    first_name varchar(50),
    last_name varchar(50),
    budget integer,
    preferred_move_date date,
    address_line_1 varchar(90),
    address_line_2 varchar(50),
    city varchar(30),
    state varchar(2),
    zip varchar(5),
    phone varchar(15),
    status varchar(20),
    agent_id integer,
    sold boolean,
    created_at timestamp,
    constraint client_agent_fk
		foreign key (agent_id)
        references agents (agent_id)
        on delete cascade
		on update restrict,
	constraint check_status check(lower(status) in ('prospective', 'in progress', 'closed'))
);
    
create table appointments (
	agent_id integer NOT NULL,
    client_id integer NOT NULL,
    property_id integer NOT NULL,
    tour_datetime timestamp NOT NULL,
    outcome varchar(50),
    created_at timestamp,
    primary key (agent_id, client_id, property_id, tour_datetime),
    constraint appt_agent_fk
		foreign key (agent_id) references agents (agent_id)
        on delete cascade
		on update restrict,
	constraint appt_client_fk
		foreign key (client_id)
        references clients (client_id)
        on delete cascade
		on update restrict,
	constraint appt_prop_fk
		foreign key (property_id)
        references properties (property_id)
        on delete cascade
		on update restrict,
    constraint check_outcomes check (lower(outcome) IN ('uninterested', 'interested', 'make offer', 'buy') or outcome is null
));


insert into agents (first_name,
                    last_name,
                    address_line_1,
                    address_line_2,
                    city,
                    state,
                    zip,
                    phone,
                    start_date,
                    created_at)
values  ('Betty', 'Wainright', '122 West Bend Avenue', '', 'Bellevue', 'WA', '98443', '(365) 555-555', '2024-02-05', '2024-04-04'),
        ('Kevin', 'Standard', '5431 Alameda Boulevard', 'Apt. 303', 'Charleston', 'WV', '45551', '(403) 555-555', '2024-03-05', '2024-04-04'),
        ('Veronica', 'Withersby', '11 Front Street', 'Unit 4432', 'San Diego', 'CA', '92101', '(714) 555-555', '2024-04-05', '2024-04-04');


insert into properties  (address_line_1,
                         address_line_2,
                         city,
                         state,
                         zip,
                         original_listing_price,
                         sold_price,
                         type,
                         sqft,
                         bedrooms,
                         bathrooms,
                         year_built,
                         on_market,
                         off_market,
                         agent_id,
                         sold,
                         created_at)
values  ('485 Elliot Avenue', '', 'Eugene', 'OR', '43355', 150000, 149000, 'Single Family Home', 1800, 2, 1, 1988, '2024-02-05', '2024-12-31', 1, False, '2024-04-04'),
        ('6767 Repost Parkway', '', 'Lafayette', 'IL', '45647', 500000, 499000, 'Single Family Home', 2300, 3, 3, 2015, '2024-03-21', '2024-12-31', 1, False, '2024-04-04'),
        ('11 Brookwood Road', 'Suite 1990', 'Nutley', 'ID', '56767', 1000000, 1500000, 'Commercial', 2500, 0, 2, 2004, '2024-03-22', '2024-12-31', 1, False, '2024-04-04');


insert into clients (first_name,
                    last_name,
                    budget,
                    preferred_move_date,
                    address_line_1,
                    address_line_2,
                    city,
                    state,
                    zip,
                    phone,
                    status,
                    agent_id,
                    sold,
                    created_at)
values  ('Wayne', 'Wilson', 450000, '2024-06-30', '1400 NW 114th Avenue', '', 'Scranton', 'PA', '12344', '(543) 555-555', 'Prospective', 1, False, '2024-04-04'),
        ('Stephanie', 'Provost', 750000, '2024-07-30', '566 Withers Lane', '', 'Pittsburgh', 'PA', '23423', '(778) 555-555', 'In Progress', 1, False, '2024-04-04'),
        ('Emory', 'Strickland', 700000, '2024-03-31', '787 Silverleaf Court', 'Apt. 111', 'Cleveland', 'OH', '23434', '(554) 555-555', 'Closed', 1, True, '2024-04-04');


insert into appointments (agent_id,
                          client_id,
                          property_id,
                          tour_datetime,
                          outcome,
                          created_at)
values  (1, 1, 1, '2024-06-01 13:15:00', 'Interested', '2024-04-04'),
        (2, 2, 2, '2024-06-02 14:00:00', 'Interested', '2024-04-04'),
        (3, 3, 3, '2024-06-03 10:30:00', 'Interested', '2024-04-04');
