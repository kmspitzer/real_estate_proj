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
