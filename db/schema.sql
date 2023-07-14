
DROP TABLE IF EXISTS PASSENGERS;
CREATE TABLE PASSENGERS(
        passenger_id text primary key,
        name text not null,
        email text not null,
        password text not null,
        address text not null,
        phone integer not null
    );

INSERT INTO PASSENGERS VALUES(100001,"John","john@pms.com","john123","Mumbai",1023300112);
INSERT INTO PASSENGERS VALUES(100002,"Bob","bob@pms.com","bob123","Delhi",1023399882);
INSERT INTO PASSENGERS VALUES(100003,"Rahul","rahul@pms.com","rahulxyz","Trivandrum",1778399882);
INSERT INTO PASSENGERS VALUES(100004,"Ria","ria@pms.com","ria@789","Bangalore",1112399882);
INSERT INTO PASSENGERS VALUES(100005,"Alice","alice@pms.com","alice@789","Kolkata",1112301082);

DROP TABLE IF EXISTS BOOKINGS;
CREATE TABLE BOOKINGS(
    pnr_number text primary key,
    passenger_id text not null references passengers(passenger_id),
    travel_date text not null,
    source_airport text not null,
    destination_airport text not null,
    status integer not null references booking_status_master(status),
    seat_preference integer not null references seat_preference_master(seat_preference),
    meal_preference integer not null references meal_preference_master(meal_preference)
);

INSERT INTO BOOKINGS VALUES(4637672631,100001,"2023-07-07","Mumbai","Hyderabad",1,3,2)
INSERT INTO BOOKINGS VALUES(4637672634,100001,"2023-07-12","Hyderabad","Mumbai",1,3,2)
INSERT INTO BOOKINGS VALUES(4637672642,100002,"2023-08-09","Chennai","Goa",1,3,2)
INSERT INTO BOOKINGS VALUES(4637672678,100002,"2023-07-10","Goa","Delhi",1,3,2)
INSERT INTO BOOKINGS VALUES(4637672689,100003,"2023-07-11","Bangalore","Mumbai",1,3,2)
INSERT INTO BOOKINGS VALUES(4637672611,100003,"2023-08-08","Mumbai","Kochi",1,3,2)
INSERT INTO BOOKINGS VALUES(4637672609,100004,"2023-09-09","Kochi","Kolkata",1,3,2)
INSERT INTO BOOKINGS VALUES(4637672629,100004,"2023-01-11","Kolkata","Hyderabad",1,3,2)
INSERT INTO BOOKINGS VALUES(4637672231,100005,"2023-27-07","Indore","Bhubaneswar",1,3,2)
INSERT INTO BOOKINGS VALUES(4637672991,100005,"2023-29-07","Bhubaneswar","Delhi",1,3,2)

DROP TABLE IF EXISTS BOOKING_STATUS_MASTER;
CREATE TABLE BOOKING_STATUS_MASTER(
    status integer primary key,
    status_value text not null
)

INSERT INTO BOOKING_STATUS_MASTER VALUES(1,"New");
INSERT INTO BOOKING_STATUS_MASTER VALUES(2,"Hold");
INSERT INTO BOOKING_STATUS_MASTER VALUES(3,"Confirmed");

DROP TABLE IF EXISTS SEAT_PREFERENCE_MASTER;
CREATE TABLE SEAT_PREFERENCE_MASTER(
    seat_preference integer primary key,
    preference_value text not null
)

INSERT INTO SEAT_PREFERENCE_MASTER VALUES(1,"Aisle");
INSERT INTO SEAT_PREFERENCE_MASTER VALUES(2,"Middle");
INSERT INTO SEAT_PREFERENCE_MASTER VALUES(3,"Window");

DROP TABLE IF EXISTS MEAL_PREFERENCE_MASTER;
CREATE TABLE MEAL_PREFERENCE_MASTER(
    meal_preference integer primary key,
    preference_value text not null
)

INSERT INTO MEAL_PREFERENCE_MASTER VALUES(1,"Veg");
INSERT INTO MEAL_PREFERENCE_MASTER VALUES(2,"Non Veg");

-- select b.pnr_number, b.travel_date, b.source_airport, b.destination_airport, b.seat_preference, b.meal_preference, p.name, p.email, p.phone
-- from Passengers p, Bookings b where p.passenger_id = b.passenger_id;