# TONY LE HUYNH - GCAB012201 - WEB SERVER API ASSIGNMENT


To start the application, ensure that the .env file is adjusted.

The below line of code needs to be changed according to the database details
```
DATABASE_URL="postgresql+psycopg2://postgres:123456@localhost:5432/postgres"
```

Once virtual environment is activate, run these commands in the terminal - flask db drop, flask db create and flask db seed in order to create and seed the database tables.

Then run the command in the terminal - flask run - in order to run the application. 

## _R1_ 

The problem being solved by this application is that of tracking song credits - in particular the collaborators on songs. 

Despite typically seeing only one artist's name tied to songs, the majority of songs have multiple collaborators. There are many pop songs that have multiple songwriters. Along with this are producers and instrumentalists that collaborate to bring a song idea to life. Typically there will also be a vocalist, a singer or rapper, on a track who will be recorded by a recording engineer. Once everything has been recorded, the song will typically be mixed by a mixing engineer and then mastered by a different mastering engineer. 

This shows that there are many people that are involved with seeing a song come to life, before the song even reaches the ears of the public. This also means that there are many people who will need to be included on the song's credits list, and also compensated accordingly in the form of fees or royalties. 

As it can be difficult to keep track of all collaborators who were involved in a song, this particular API Web Server application will be of assistance. Users can register themselves as musicians, classified by the type of musician they are such a drummer or vocalist, and then record their contribution to a song. This application will help track all the collaborators on a song. Furthermore, a lot of musicians are associated with record labels (which adds to further complexity in terms of the splitting of payments as there can be many people such as lawyers and publicists on a label team), which is why record labels that musicians are associated with can be tracked on this application too. 

Overall, the application will help solve how difficult it can be to keep track of a song's credits when there can be multiple collaborators on one song, across time. Therefore, the application will make it much more easy and convenient to track contributions/credits made to a song. 

## _R2_

The reasons this particular problem of tracking song credits needs solving, is due to both fairness and legality. 

It is simply the right and fair thing to do when properly crediting those who have contributed to a song, or any project in particular. This is so that people are properly acknowledged and credited for their hard work. Also, being credited is very important for peoples' careers as this can help people find other work as well. 

Furthermore, the music industry is built on trust and relationships. Artists collaborate with each other in good faith. If someone does not get fairly credited for their work, this can damage professional relationships as well as industry reputation. The musician will no longer want to work with the artist. Word can also spread in the industry, which can damage the artist's reputation and their future possibilities of having other collaborators work with them. Not only this, but if word spreads to the public then the artist's public reputation can also be damaged as well. Overall, it is important that all collaborators on songs are properly acknowledged and credited to preserve trust and relationships that have been built. 

Another issue is the legality when it comes to crediting collaborators. Artists' and record labels have a legal obligation to credit and properly compensate collaborators.

As mentioned before, there are many collaborators who are typically involved with the making of a song. These include people such as songwriters, instrumentalists (drummer, bassist, guitarist, pianist etc.), producers, vocalists (singers & rappers), recording engineers, mixing engineers and mastering engineers. 

Depending on the business arrangement, each collaborator will have their own fee or will be entitled to a percentage royalty of the song. Once a song has been completed and submitted to be released to the public, collaborators will need to be compensated accordingly. 

Failure to properly financially compensate collaborators can result in legal issues for the artist, their team and their record label. Legal disputes can be very time consuming and result in heavy costs due to legal fees. Therefore, it is important that this issue is avoided altogether. 

Overall, it is important to keep track of collaborators in the making of songs in order to properly credit them both in writing and financially. The reason I have all this information is due to the fact that I've worked in the music industry myself and also have many friends in the music industry. 

The making of a song can take months, let alone years for some songs. Many artists also travel or work online by sending files, resulting in collaborators potentially being from all across the world. In this time, things can become lost or forgotten. Different collaborators could have different records of contributions, on different computers, in different studios across the world. With the large amount of collaborators on songs, it can be very difficult to keep track of who worked on a song and what their contribution was. 

This is why these problems presented above, can be addressed through the building of this API Webserver Project - where the collaborators/credits for the song making process will tracked and recorded. The application will make the process of keeping a record of the credits + contributions easier and more efficient, in a central location. Musicians will be able to see what credits they have on songs. Record Labels associated with the musicians can also keep a track of this as well. And overall, all the credits/contributions for each song from different musicians, will easily be able to be recorded, tracked and shown.

## _R3_

The database management system chosen for this API Webserver Project will be PostgreSQL. PostgreSQL is an open source relational database management system, that supports both SQL (relational) and JSON (non-relational) querying (Reference 1). 

PostgreSQL has a strong industry reputation for it's architecture, reliability, scalability, robust feature set, extensibility and data integrity (Reference 4). All of these qualities are very beneficial for an API Webserver application and shows how PostgreSQL's widespread use in the industry means it can be relied on for this API Webserver project as well.  

There are many other reasons and benefits why PostgreSQL is a suitable choice for this particular API Webserver project.

Firstly, PostgreSQL is supported on all platforms (Windows, Linux, Mac) which means that anyone working on the API Webserver Project should be able to utilise PostgreSQL (Reference 4)

PostgreSQL is also free with no licensing cost as well as being under an open source license. Once again, this is a benefit for the API Webserver Project as anyone working on this project will be able to use PostgreSQL for free due to the cost-effectiveness that PostgreSQL provides. PostgreSQL can also be used, modified and implemented freely as per the project's requirements. As there are no licensing fees or restrictions, deployment can also be scaled based on the application's needs without having to worry about any financial burdens of the database management system (Reference 2). This also further highlights the extisbility aspect of PostgreSQL. Also code can be written from different programming languages without needing to recompile the database with PostgreSQL (Reference 4). This also means that PostgreSQL can be tailored as a database to the specific API Webserver application requirements. 

As per the documentation of PostgreSQL, these are some of the data types and data integrity aspects of PostgreSQL (Reference 4):

__Data Types__
- Integer, Numeric, String, Boolean
- Date/Time, Array, Range
- JSON/JSONB, XML, Key-value (Hstore)

__Data Integrity__
- UNIQUE, NOT NULL
- Primary Keys
- Foreign Keys

These data types and integrity aspects are very useful for the API Webserver application, hence another benefit for using PostgreSQL. Furthermore, custom data types, operators and functions can also be defined with PostgreSQL. This once again highlights how PostgreSQL can be customised and adapted to the specific needs of the API Webserver application. 

Learning PostgreSQL also doesn't require a lot of training, meaning it will be easy to learn and use for the API Webserver Project (Reference 3).

PostgreSQL is widely used, and is well documented and supported. As PostgreSQL is open-source, it has an active community that contributes to its continuous improvement - providing valuable resources such as documentation, tutorials and troubleshooting support (Reference 1). This is a further benefit for the API Webserver Project, as any issues that arise can be addressed by the active community around PostgreSQL. 

PostgreSQL is highly scalable both in the large quantity of data it can manage and in the number of concurrent users it can accommodate (Reference 1). This aspect is important as the API Webserver has the potential to be scaled to have large quantities of data and a large number of users in the future. Thus PostgreSQL is a viable option the project due to it's scalability. 

PostgreSQL’s write ahead logging makes it a highly fault-tolerant database, thus highlighting the reliability of PostgreSQL as a database management system for the API Webserver (Reference 1). PostgreSQL can be relied on to continue operating correctly and maintain data consistency and availability, even in the face of unexpected hardware failures, software crashes, errors or malfunctions (Reference 2). This is also due to the fact that PostgreSQL is ACID compliant (Atomicity, Consistency, Isolation, and Durability), ensuring that transactions are consistent, isolated and durable (Reference 2). This is essential for the API Webserver application which requires data integrity and reliability to be upheld by PostgreSQL. 

PostgreSQL offers performance related features such as Just-In-Time (JIT) compilation, parallelization of read queries and indexing (Reference 4). This once again is a benefit for the API Webserver Application as PostgreSQL will be a suitable choice for quick and efficient data processing.

Lastly, PostgreSQL offers key security features will prove useful for the API Webserver application being built. These include features such as authentication, access control and also column & row level security. These security features are key in the use of the API Webserver application where the control of data access and securityy are important - thus further justifying the use of PostgreSQL.

Though PostgreSQL has many benefits, there are some drawbacks that it has when compared to other database systems. 

One disadvanage is that a lot of open source apps support another popular relational database system called MySQL, however there may not be as much support for PostgreSQL (Reference 2).

On a few performance metrics, PostgreSQL has been noted to be slower than MySQL as well (Reference 2).

As PostgreSQL is open-source and free, there isn't a dedicated user/customer support team available to assist with any queries you may have as opposed to if you were using a paid database system. This can be seen as a disadvantage however it is worth to note that there is extensive official documentation for PostgreSQL as well as it having a large and active community. 

Another point of note is that PostgreSQL does have some capacity for graph and spatial data, however this isn't as extensive as other databases which were specifically designed to support these types of data (Reference 3). In particular, database systems such as Neo3j and PostGIS are more suited for applications that require more comprehensive graph and spatial capabilities from the database system. This should not be a huge issue for the API Webserver application as the application being built will not utilise graph and spatial data. Furthermore, should the application require these types of data, then use of multiple database systems is a possibility rather than having to solely rely on only one. 

Overall, there are a large array of benefits for PostgreSQL as a database management system. Though it has a small number of drawbacks, PostgreSQL is very well suited for use in the API Webserver application being built. 

## _R4_

ORM stands for Object Relational Mapping. This is a technique for appications to interact with relational databases in an object-oriented manner. Instead of writing plain SQL queries, developers can interact with the database using the programming language that was used to code their application - through use of ORM tools (Reference 6)

The primary ORM tool that will be used for this API Webserver application will be SQLAlchemy, which is best suited for Python applications built in Flask (Reference 6).

**Below are key functionalities of an ORM:**

_Data Modeling_

An ORM such as SQLAlchemy can allow the structure of a database schema to be defined in the code of the application itself. This is a benefit as it the approach is more intuitive and flexible than writing raw SQL queries. For example with SQLAlchemy, tables and columns in the database schema can be defined as Python classes and attributes. This also makes it more convenient and easier to maintain the database and its consistency, and make changes to the schema without having to directly modify the database (Reference 6). ORMs can also provide tools for validating the database schema and detect inconsistencies or errors in the schema definition. ORMs can also provide tools for managing cascading updates or deletes across related tables, thus further helping to maintain database integrity and consistency. 

_Data Persistence_

ORMs make it easier to persist data to the database, such as creating tables, seeding the tables with data and executing SQL queries. Developers are able to perform CRUD (Create, Read, Update, Delete) operations on the database through use of an ORM (Reference 7). Tables in a database are able to be created, modified and deleted through use of an ORM as well. 

_Querying_

A key functionality of an ORM such as SQLAlchemy, is that database queries are able to be written in the programming language of the application, such as Python, rather than writing SQL queries. Python code can be written for an application, and the ORM will generate the corresponding SQL queries and execute them and interact with the database(Reference 6). SQLAlchemy provides a database abstraction layer that allows developers to interact with databases using an object-oriented approach. Another way to describe this is that SQLAlchemy provides a SQL Expression Language, allowing complex SQL queries to be written using a Pythonic syntax. 

ORMs such as SQLAlchemy also provide advanced querying capabilities, with complex queries involving multiple tables able to be handled. This includes tasks such as filtering, sorting and grouping data, as well as complex joins and subqueries (Reference 8). 

When interacting with databases, ORMs such as SQLAlchemy also utilise a method called connection pooling. This is where existing database connections are reused rather than creating a new one, thus helping improve the performance and efficiency of applications interacting with database systems (Reference 8). 

Overall, it is easier to read and write queries that interact with the relational database through use of an ORM. ORMs abstract the details of database operations, including the generation of SQL queries, executing them, and parsing the results. 

_Relationships_

An important aspect of relational databases are the relationships between tables in the database. An ORM provide a convenient way for these relationships between tables in the database to be defined and managed, which is especially important for data models with many-to-many or one-to-many relationships. ORMs allow you to define relationships between classes by defining attributes that reference other classes (Reference 7). 

In particular with SQLAlchemy, database tables can be defined using Python classes and attributes, along with the relationships that tables can have between each other through the use of features such as primary and foreign keys (Reference 7). Relationships can also be defined through the db.Relationship function in SQLAlchemy, as well as the use of backref. 

_Migrations_

Database migrations can also be managed by ORMs, where the modification of the schema of a database over time without losing data is made easier. This is where code written in a programming language, such as Python in the example of using SQLAlchemy, can be written to make changes to the database schema and then executed to apply the changes to the overall database. ORMs can ensure that the integrity of the database is maintained and that data is not lost and errors are handled during the modifications made to the database schema (Reference 6).

_Database and Web Framework Integration_

 ORMs such as SQLAlcehmy support multiple different database systems, such as PostgreSQL, MySQL and Oracle, therefore allowing the ability to work with a wide range of databases using a consistent API. Furthermore, tools can be provided by ORMs like SQLAlchemy, to integrate with web frameworks like Flask for web applications. 

**There are also many key benefits of an ORM:**

_Productivity and efficiency_

ORMs make it so that there an application will require less and cleaner code compared to having to use embedded SQL (Reference 5). This helps improve productivity as less code will need to be written to interact with the database, hence reducing the likelihood of bugs and making applications easier to build. Furthermore, with an ORM, there is no need to convert from a table to object and vice versa (Reference 5). Thus this makes the implementation of ORMs in applications simply to use and maintain.

Another key benefit is that there isn't a need to write SQL statements when using an ORM. The chosen programming language of choice for a developer can be used to interact with a database system instead, through use of an ORM. 

_Portability_

Through use of an ORM, the code written to interact with a database usually remains the same, or will only require minor changes, if different databases are used or changed (Reference 5). This is beneficial, especially in cases where applications require having multiple database backends. Switching between different databse systems is made easier due to ORMs. 

_Features_

Depending on the ORM used, there can be a range of advanced features that are offered. These include features such as support for transactions, connection pooling, migrations, seeds and streams (Reference 9).

_Scalability_

An ORM can help optimise database queries and the number of database connections, through the use of methods such as connnection pooling (Reference 6). ORMs can also provide tools to assist wih distributing database load across multiple services. Thus, the performance application and load on the database server are improved and therefore the scalability of applications can be optimised through using ORMs. 

_Testing_

The use of an ORM can make it easier to write and execute tests. This is because code written in an application using an ORM can be tested without having to interact with the database (Reference 6). 


## R5

The endpoint documentation for this API Webserver Application will be separated into the following categories, representing the files in the controller structure of the application: musicians_controller, labels_controller, songs_controller and credits_controller.


Below are also the steps for authentication. 


AUTHENTICATION 
- Most of the updating/deleting in the database will be done by the Admin user only. 
- An Access token will be generated and returned when a musician logs in. The Admin user details are below.
- Access token generated, can then be pasted into the Authorization header of an API testing platform (I used Postman), in the Bearer Token section. 
- This will allow you to be authenticated by the API application, and then be able to execute the HTTP verbs which are restricted to admin musician users only (typically updating and deleting queries.)

To log in and authenticate as the admin musician user:

- VERB: POST
- URL: http://localhost:5000/musician/login
- Admin musician user login details are:
```JSON
{
    "email": "admin@admin.com",
    "password": "123456"
}
```

Expected return output is:

```JSON
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3OTE1MDg5MCwianRpIjoiOGJhNGIxZDAtYTBjNS00NjhmLTkzZTEtNjg0ZWYzYmE2YTI1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE2NzkxNTA4OTAsImV4cCI6MTY3OTIzNzI5MH0._l6MIoqN4vp5cy_I3pTPdelRfLB9peSDmwy0pA3ycUY",
    "email": "admin@admin.com",
    "message": "Musician logged in successfully"
}
```

Screenshot of how to paste access_token provided in the Authorization header (bearer token selection) section of Postman API Platform:


![Authorisation Postman screenshot](./docs/Authorisation.jpg)


Here is also a screenshot of how to provide raw JSON data in the Body, in order to provide the desired inputs. This will be useful to follow to provide the necessary information for things such as registering, adding and updating a new musician, song, credit, and label. 

![Authorisation Postman screenshot](./docs/Authorisation_2.jpg)

__MUSICIANS_CONTROLLERS ENDPOINTS__

*GET ROUTES - HTTP VERB: GET*

**1.** 
- Verb: GET
- URL route: http://localhost:5000/musician/list
- No authentication
- No need to provide any raw JSON data.
- Expected response data: Shows list of all musicians in the database with their details (email, first_name, last_name, id, label_id, phone_number, profession). Admin user is excluded from this list

**1.1** 

Also able to further filter by profession when geting a list of all musicians
- Example URL route: http://localhost:5000/musician/list?profession=Singer
- Verb: GET
- Returns only musicians whose profession is "Singer". In the example seeded data, the musician id returned is 2 and name is Frank Ocean.
- Other professions include "Drummer", "Rapper", "Songwriter", "Producer" etc. 

Example return for where profession is = "Singer"
```JSON
[
    {
        "email": "frank@email.com",
        "first_name": "Frank",
        "id": 2,
        "label_id": 4,
        "last_name": "Ocean",
        "phone_number": "404",
        "profession": "Singer"
    }
]
```

**2.**
- Verb: GET
- URL route: http://localhost:5000/musician/with_label
- No auth
- Returns list of all musicians who have a label_id, which means they are associated with a label (Record label)

Example return:
```JSON
[
    {
        "email": "frank@email.com",
        "first_name": "Frank",
        "id": 2,
        "label_id": 4,
        "last_name": "Ocean",
        "phone_number": "404",
        "profession": "Singer"
    },
    {
        "email": "mike@email.com",
        "first_name": "Mike",
        "id": 3,
        "label_id": 1,
        "last_name": "Dean",
        "phone_number": "404",
        "profession": "Producer"
    },
    {
        "email": "jack@email.com",
        "first_name": "Jack",
        "id": 4,
        "label_id": 3,
        "last_name": "Antonoff",
        "phone_number": "404",
        "profession": "Songwriter"
    },
    {
        "email": "steve@email.com",
        "first_name": "Steve",
        "id": 5,
        "label_id": 2,
        "last_name": "Lacey",
        "phone_number": "404",
        "profession": "Guitarist"
    },
    {
        "email": "kenny@email.com",
        "first_name": "Kenny",
        "id": 7,
        "label_id": 2,
        "last_name": "Beats",
        "phone_number": "404",
        "profession": "Pianist"
    },
    {
        "email": "thunder@email.com",
        "first_name": "Thunder",
        "id": 8,
        "label_id": 3,
        "last_name": "Cat",
        "phone_number": "404",
        "profession": "Bassist"
    },
    {
        "email": "anderson@email.com",
        "first_name": "Anderson",
        "id": 9,
        "label_id": 3,
        "last_name": "Paak",
        "phone_number": "404",
        "profession": "Drummer"
    }
]
```

**3.**
- Verb: GET
- URL route: http://localhost:5000/musician/no_label
- No auth
- Returns list of all musicians who don't have a label_id, which means they are not associated with a label. label_id fields will be null 

Example return:
```JSON
[
    {
        "email": "jeff@email.com",
        "first_name": "Jeff",
        "id": 10,
        "label_id": null,
        "last_name": "Ellis",
        "phone_number": "404",
        "profession": "Mixing Engineer"
    },
    {
        "email": "dave@email.com",
        "first_name": "Dave",
        "id": 11,
        "label_id": null,
        "last_name": "Pensado",
        "phone_number": "404",
        "profession": "Mastering Engineer"
    },
    {
        "email": "tyler@email.com",
        "first_name": "Tyler",
        "id": 6,
        "label_id": null,
        "last_name": "Okonma",
        "phone_number": "404",
        "profession": "Rapper"
    }
]
```

**4.**
- VERB: GET
- URL route: 
```
http://localhost:5000/musician/<int:musician_id>/credits
```
- EXAMPLE URL: http://localhost:5000/musician/3/credits
- No auth
- Retrieves a musician by their ID, provided in URL, and then returns a list of all credits that the musician is associated with. The example for musician_id 3 returns Mike Dean, and they have 4 credits associated with them.

Expected return for the example URL above
```JSON
{
    "credits": [
        {
            "contribution_date": "2011-01-01",
            "description": "Vocals, lyrics",
            "id": 1,
            "musician_email": "mike@email.com",
            "musician_id": 3,
            "song_id": 1,
            "song_title": "Ivy"
        },
        {
            "contribution_date": "2014-03-03",
            "description": "Vocals, lyrics",
            "id": 2,
            "musician_email": "mike@email.com",
            "musician_id": 3,
            "song_id": 4,
            "song_title": "911"
        },
        {
            "contribution_date": "2015-01-01",
            "description": "Vocals, lyrics",
            "id": 3,
            "musician_email": "mike@email.com",
            "musician_id": 3,
            "song_id": 5,
            "song_title": "Biking"
        },
        {
            "contribution_date": "2014-12-11",
            "description": "Vocals, lyrics",
            "id": 4,
            "musician_email": "mike@email.com",
            "musician_id": 3,
            "song_id": 6,
            "song_title": "Thinkin Bout You"
        }
    ],
    "musician_name": "Mike Dean"
}
```


**4.1**
You can also filter by contribution_date(year). Intention is that the musician can search the credits they've done, and also provide the year in the URL, which returns the credits they did in a certain year

- EXAMPLE URL: http://localhost:5000/musician/3/credits?contribution_date=2014
- This will return Musician 3's associated credits, where the contribution date was in the year 2014. For the example data, two credits are returned with credit_id = 2 and credit_id = 4

```JSON
{
    "credits": [
        {
            "contribution_date": "2014-03-03",
            "description": "Vocals, lyrics",
            "id": 2,
            "musician_email": "mike@email.com",
            "musician_id": 3,
            "song_id": 4,
            "song_title": "911"
        },
        {
            "contribution_date": "2014-12-11",
            "description": "Vocals, lyrics",
            "id": 4,
            "musician_email": "mike@email.com",
            "musician_id": 3,
            "song_id": 6,
            "song_title": "Thinkin Bout You"
        }
    ],
    "musician_name": "Mike Dean"
}
```


*POST ROUTES - HTTP VERB: POST*

**5.**
- VERB: POST
- URL route: 
```
http://localhost:5000/musician/register
```
- No auth
- Will be required to supply information via Body, and raw JSON data
- Provide data to register user. label_id by default is None, so if label_id isn't provided then the user will still be able to successfully register. Furthermore, if user provides a label_id that doesn't exist, then this will be flagged. 

Required inputs are:
- "email": string
- "password": string
- "first_name": string
- "last_name": string
- "profession": string
- "phone_number": string

Optional input:
- "label_id": integer

Here is an example raw JSON data input included in the body, to register a musician:

```JSON
{
    "email": "sam@email.com",
    "password": "123456",
    "first_name": "Sam",
    "last_name": "Smith",
    "profession": "Singer",
    "phone_number": "222",
    "label_id": 2
}
```

It should return access token, email and message saying musician registered successfully.

```JSON
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3OTE1MDY3MywianRpIjoiNzA1NGM1MmYtMTE3NS00MDljLWIxNmEtMTA3YjQzNGIzYTRhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjE0IiwibmJmIjoxNjc5MTUwNjczLCJleHAiOjE2NzkyMzcwNzN9.7Wu4sq0z6jfAgkXAsmBZT-HlDxpK5eSXsoDDr-DSyBY",
    "email": "sam@email.com",
    "message": "Musician registered successfully"
}
```

**6.**
- VERB: POST
- URL: 
```
http://localhost:5000/musician/login
```
- Required data is the email and password. See below example for the admin user. Once again provided as raw JSON data in the body. 

```JSON
{
    "email": "admin@admin.com",
    "password": "123456"
}
```
Returns the below as an example:
```JSON
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3OTE1MDg5MCwianRpIjoiOGJhNGIxZDAtYTBjNS00NjhmLTkzZTEtNjg0ZWYzYmE2YTI1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE2NzkxNTA4OTAsImV4cCI6MTY3OTIzNzI5MH0._l6MIoqN4vp5cy_I3pTPdelRfLB9peSDmwy0pA3ycUY",
    "email": "admin@admin.com",
    "message": "Musician logged in successfully"
}
```

*PUT ROUTE ENDPOINT - HTTP VERB: PUT*

**7.**
- verb: PUT
- URL: 
```
http://localhost:5000/musician//<int:id>/
```
- Authentication is required in order to use this route to update a musician. Needs to be access token of admin user. Provided as a bearer token in the Authorization header. Further details for this included at the start of R5 in this README file. 


- Access token will be returned when logged in. Admin user details are : verb: POST,  url: http://localhost:5000/musician/login
```JSON
{
    "email": "admin@admin.com",
    "password": "123456"
}
```

- No data is mandatorily required , as I have coded it so that only the fields provided in the Body (raw JSON) will be be updated accordingly. As long as the fields provided matches the fields of the musician table, and the data inputs are in the correct format, then it will be updated successfully. For example, if only the "phone_number" field is provided, then only "phone_number" will be updated for the musician. 

- Here is an example of a JSON input I did to update Musician_ID = 9
- URL: http://127.0.0.1:5000/musician/9

Body input
```JSON
{
    "phone_number": "This is now updated",
    "profession": "Updated"
}
```
Data returned
```JSON
{
    "message": "Musician updated successfully",
    "musician": {
        "email": "frank2@email.com",
        "first_name": "Anderson",
        "id": 9,
        "label_id": 3,
        "last_name": "Paak",
        "phone_number": "This is now updated",
        "profession": "Updated"
    }
}
```
Here is another example input to test for the body raw JSON data. Password and admin status can be updated in this HTTP PUT method, as only the admin user can use this update PUT verb endpoint. 
```JSON
{
    "first_name": "Update",
    "last_name": "Update",
    "email": "Update",
    "profession": "Update",
    "phone_number": "Update",
    "password": "123456789",
    "label_id": 2,
    "admin": true
}
```

*DELETE ROUTE ENDPOINT - HTTP VERB: DELETE*

**7.**

- verb: DELETE
- Authorization is required in order to delete musician. Bearer token needs to be provided in the Authorization header. Admin user details and login details are found above, to get access token (as well as the start of R5 in this README doc)
- Required data is simply just the URL provided. No need for JSON data in the body.
URL format is
```
http://localhost:5000/musician/<int:id>/
```

Here is an example URL to delete musician_id = 9:

url: http://localhost:5000/musician/9

Here is the response data after successful deletion. Message provided indicated deleted successfully and deleted musician details are shown:

```JSON
{
    "message": "Musician deleted successfully",
    "musician": {
        "email": "Update",
        "first_name": "Update",
        "id": 9,
        "label_id": 2,
        "last_name": "Update",
        "phone_number": "Update",
        "profession": "Update"
    }
}
```

__LABELS_CONTROLLERS ENDPOINTS__

*GET ROUTES - HTTP VERB: GET*

**1.** 
- Verb: GET
- URL is
```
 http://localhost:5000/labels
 ```
- No auth required or raw JSON data in the body. 
- Expected response data is below:

```JSON
[
    {
        "id": 1,
        "name": "Warner Records",
        "type": "Major"
    },
    {
        "id": 2,
        "name": "Sony Records",
        "type": "Major"
    },
    {
        "id": 3,
        "name": "Universal Records",
        "type": "Major"
    },
    {
        "id": 4,
        "name": "Blonded Records",
        "type": "Independent"
    },
    {
        "id": 5,
        "name": "Golf Records",
        "type": "Independent"
    }
]
```
This query should a return a list of all the labels in the database, and their details.

**2.** 
- Verb: GET
- URL is:
```
http://localhost:5000/labels//<int:label_id>/musicians
```
- This query will return all the musicians that are associated with the label, based on the label id provided in the URL. This is a one to many relationship, so this will return all the musicians that have label_id as a foreign key in the musicians table. 

- Here is an example URL where label_id = 3 is queried: http://localhost:5000/labels/3/musicians

Return data 
```JSON
[
    {
        "email": "jack@email.com",
        "first_name": "Jack",
        "id": 4,
        "label_id": 3,
        "last_name": "Antonoff",
        "phone_number": "404",
        "profession": "Songwriter"
    },
    {
        "email": "thunder@email.com",
        "first_name": "Thunder",
        "id": 8,
        "label_id": 3,
        "last_name": "Cat",
        "phone_number": "404",
        "profession": "Bassist"
    },
    {
        "email": "anderson@email.com",
        "first_name": "Anderson",
        "id": 9,
        "label_id": 3,
        "last_name": "Paak",
        "phone_number": "404",
        "profession": "Drummer"
    }
]
```
**2.1**
- verb: GET
- Can also filter the above query by profession. So a label can query the musicians that are associated with them, and then filter that by their profession.
- The example below, label_id = 3, queries to find the musicians associated with the label whose profession is = "Drummer".

- Example URL - http://localhost:5000/labels/3/musicians?profession=Drummer

Return data (only returns musician with profession = "Drummer")
```JSON
[
    {
        "email": "anderson@email.com",
        "first_name": "Anderson",
        "id": 9,
        "label_id": 3,
        "last_name": "Paak",
        "phone_number": "404",
        "profession": "Drummer"
    }
]
```

*POST ROUTE - HTTP VERB: GET*

**3.** 
- Verb: POST
- URL is http://localhost:5000/labels/create
- Auth is required to create a new label as only admin can create a new label. Bearer token to be provided in Authorization header (Postman was used by me), generated by logging in as the admin user. Admin details provided previously
- Required input data is in the body as raw JSON. 
- Required fields are "name" and "type", with both associated with string values. 

See below an example of an input to create a new label:
```JSON
{
    "name": "New Label",
    "type": "New"
}
```

Expected return data:
```JSON
{
    "label": {
        "id": 6,
        "name": "New Label",
        "type": "New"
    },
    "message": "Label created successfully"
}
```


*PUT ROUTE ENDPOINTS - HTTP VERB: PUT*

**4.** 
- Verb: PUT
- URL is
```
 http://localhost:5000/labels//<int:id>/
```
- Auth is required to update label as only admin can update label. Bearer token to be provided in Authorization header (Postman was used by me), generated by logging in as the admin user. Admin details provided previously
- Required input data is in the body as raw JSON. 
- Required fields are "name" and "type", with both associated with string values. 

Example URL - http://localhost:5000/labels/5

See below an example of an input to update label_id = 5:
```JSON
{
    "name": "Updated",
    "type": "Updated"
}
```

Expected return data:
```JSON
{
    "label": {
        "id": 5,
        "name": "Updated",
        "type": "Updated"
    },
    "message": "Label updated successfully"
}
```

*DELETE ROUTE ENDPOINTS - HTTP VERB: DELETE*

**5.** 
- Verb: DELETE
- URL is
```
 http://localhost:5000/labels//<int:id>/
```
- Auth is required to update label as only admin can delete a label. Bearer token to be provided in Authorization header (Postman was used by me), generated by logging in as the admin user. Admin details provided previously
- No required input data in the body, only URL is required with valid id for label_id


Example URL to delete label_id = 5 -> http://localhost:5000/labels/5


Expected return data:
```JSON
{
    "label": {
        "id": 5,
        "name": "Updated",
        "type": "Update"
    },
    "message": "Label deleted successfully"
}
```

__SONGS_CONTROLLERS ENDPOINTS__

*GET ROUTE ENDPOINTS - HTTP VERB: GET*

**1.** 
- Verb: GET
- URL is
```
http://localhost:5000/songs/
```
- No other required input or auth
- Will return all songs in database with their details 

Expected return data:
```JSON
{
[
    {
        "date_finished": "2016-08-01",
        "duration": "00:04:09",
        "genre": "Alternative",
        "id": 1,
        "title": "Ivy"
    },
    {
        "date_finished": "2022-01-30",
        "duration": "00:03:52",
        "genre": "Pop",
        "id": 2,
        "title": "Bad Habit"
    },
    {
        "date_finished": "2016-06-06",
        "duration": "00:02:54",
        "genre": "RNB",
        "id": 3,
        "title": "Suede"
    },
    {
        "date_finished": "2017-08-08",
        "duration": "00:04:15",
        "genre": "Rap",
        "id": 4,
        "title": "911"
    },
    {
        "date_finished": "2017-09-09",
        "duration": "00:04:37",
        "genre": "RNB",
        "id": 5,
        "title": "Biking"
    },
    {
        "date_finished": "2012-06-11",
        "duration": "00:03:20",
        "genre": "Pop",
        "id": 6,
        "title": "Thinkin Bout You"
    }
]
}
```

**2.** 
- Verb: GET
- URL is
```
http://localhost:5000/songs/<genre>
```
- No other required input or auth
- Provide genre at the end of the URL and it will provide songs that are in that genre


Example URL for genre = "RNB" -> http://localhost:5000/songs/RNB

Expected return data:
```JSON
[
    {
        "date_finished": "2016-06-06",
        "duration": "00:02:54",
        "genre": "RNB",
        "id": 3,
        "title": "Suede"
    },
    {
        "date_finished": "2017-09-09",
        "duration": "00:04:37",
        "genre": "RNB",
        "id": 5,
        "title": "Biking"
    }
]
```

**3.** 
- Verb: GET
- URL is
```
http://localhost:5000/songs/year/<int:year>
```
- No other required input or auth
- This will return all songs that have a "date_finished" in the year included in the URL.

Example URL for songs that were finished in 2016 -> http://localhost:5000/songs/year/2016

Expected return data:
```JSON
[
    {
        "date_finished": "2016-08-01",
        "duration": "00:04:09",
        "genre": "Alternative",
        "id": 1,
        "title": "Ivy"
    },
    {
        "date_finished": "2016-06-06",
        "duration": "00:02:54",
        "genre": "RNB",
        "id": 3,
        "title": "Suede"
    }
]
```

**4.** 
- Verb: GET
- URL is
```
http://localhost:5000/songs/duration/<int:minutes>
```
- No other required input or auth
- This will return all songs that have a "duration" (in minutes), as included in the URL.

Example URL for songs that are between 4:00 minutes and 4:59 minutes -> http://localhost:5000/songs/duration/4

Expected return data:
```JSON
[
    {
        "date_finished": "2016-08-01",
        "duration": "00:04:09",
        "genre": "Alternative",
        "id": 1,
        "title": "Ivy"
    },
    {
        "date_finished": "2017-08-08",
        "duration": "00:04:15",
        "genre": "Rap",
        "id": 4,
        "title": "911"
    },
    {
        "date_finished": "2017-09-09",
        "duration": "00:04:37",
        "genre": "RNB",
        "id": 5,
        "title": "Biking"
    }
]
```

**5.** 
- Verb: GET
- URL is
```
http://localhost:5000/songs/<int:song_id>/credits
```
- No other required input or auth
- This will return all the credits that are associated with a specific song. The song is specified via the song_id provided in the URL 

Example URL for displaying all credits associated with song_id = 1 -> http://localhost:5000/songs/1/credits

Expected return data:
```JSON
{
    "credits": [
        {
            "contribution_date": "2011-01-01",
            "description": "Vocals, lyrics",
            "id": 1,
            "musician_email": "mike@email.com",
            "musician_id": 3,
            "song_id": 1,
            "song_title": "Ivy"
        },
        {
            "contribution_date": "2011-01-01",
            "description": "Mixing",
            "id": 15,
            "musician_email": "dave@email.com",
            "musician_id": 11,
            "song_id": 1,
            "song_title": "Ivy"
        },
        {
            "contribution_date": "2023-01-01",
            "description": "Mastering",
            "id": 16,
            "musician_email": "frank@email.com",
            "musician_id": 2,
            "song_id": 1,
            "song_title": "Ivy"
        }
    ],
    "song_title": "Ivy"
}
```

*POST ROUTE ENDPOINTS - HTTP VERB: POST*

**6.** 
- Verb: POST
- URL is
```
http://localhost:5000/songs/create
```
- You are not required to be an admin to create a song however you will need to login as a musician and provide your access token, in the Authorization header as a bearer token.
- To login as musician "Admin", simply follow the steps provided at the start of the R5 section. 

- Other necessary required input data are the "title" and "genre" with string values associated - in the body as raw JSON. 
- Non mandatory fields include "duration" with associated time value and "date_finished" with associated date value. These are not necessary to provide in order to create a new song.

Example input data to create a new song

```JSON
{
    "title": "New Song!",
    "genre": "New",
    "date_finished": "2023-01-01",
    "duration": "00:03:30"
}
```

Expected return response data:
```JSON
{
    "message": "Song created successfully",
    "song": {
        "date_finished": "2023-01-01",
        "duration": "00:03:30",
        "genre": "New",
        "id": 8,
        "title": "New Song!"
    }
}
```

*PUT ROUTE ENDPOINTS - HTTP VERB: PUT*

**7.** 
- Verb: PUT
- URL is
```
http://localhost:5000/songs/<int:id>/
```
- You are required to be an admin in order to update a song through this method.
- To login and provide authentication (access token in the authorization header as a bearer token) as musician "Admin", simply follow the steps provided at the start of the R5 section. 

- There is no mandatory required input data in the body section with raw JSON. The song will update according to the fields provided. For example, if the only field provided is "title", then only the song "title" will update. 

Example URL to update song_id = 1 -> http://localhost:5000/songs/1

Example input data to update all the song fields

```JSON
{
    "title": "Updated",
    "genre": "Updated",
    "date_finished": "2000-01-01",
    "duration": "00:01:11"
}
```

Expected return response data:
```JSON
{
    "message": "Song updated successfully",
    "song": {
        "date_finished": "2000-01-01",
        "duration": "00:01:11",
        "genre": "Updated",
        "id": 1,
        "title": "Updated"
    }
}
```


*DELETE ROUTE ENDPOINTS - HTTP VERB: DELETE*

**8.** 
- Verb: DELETE
- URL is
```
http://localhost:5000/songs/<int:id>/
```
- You are required to be an admin in order to delete a song through this method.
- To login and provide authentication (access token in the authorization header as a bearer token) as musician "Admin", simply follow the steps provided at the start of the R5 section. 

- No required input data in the body section with raw JSON. Only need to specify song_id in the URL to be deleted. 

Example URL to delete song_id = 2 -> http://localhost:5000/songs/2

Expected return response data:
```JSON
{
    "message": "Song deleted successfully",
    "song": {
        "date_finished": "2022-01-30",
        "duration": "00:03:52",
        "genre": "Pop",
        "id": 2,
        "title": "Bad Habit"
    }
}
```

*POST ROUTE ENDPOINTS - HTTP VERB: POST -> THIS IS FOR CREATING NEW SONG CREDITS*

**9.** 
- Verb: POST
- URL is
```
http://localhost:5000/songs/<int:id>/credit
```
- You are not required to be an admin in order to create a new credit, however you do need to login as a musician and provide your access token (in authorization header as a bearer token)
- To login and provide authentication as musician "Admin", simply follow the steps provided at the start of the R5 section. 

- Required input data in the body using raw JSON. The required fields are "description" which is associated with a string value, and "contribution_date" which is associated with a date value.

- If the credit already exists, then the credit will simply be updated according to the values provided. 

Below is an example where I have logged in as musician_id = 2. I used the access token provided after I logged in and pasted it into the bearer token section of the Authorization header. 

And then I have added a new credit to song_id = 3. 

URL used for example - http://localhost:5000/songs/3/credit

Example input data:

```JSON
{
    "description": "Added a new credit. Played trumpet on this song",
    "contribution_date": "2023-02-02"
}
```

Expected return response data:
```JSON
{
    "credit": {
        "contribution_date": "2023-02-02",
        "description": "Added a new credit. Played trumpet on this song",
        "id": 17,
        "musician_email": "frank@email.com",
        "musician_id": 2,
        "song_id": 3,
        "song_title": "Suede"
    },
    "message": "Credit for song created successfully"
}
```

__CREDITS_CONTROLLERS ENDPOINTS__

*PUT ROUTE ENDPOINTS - HTTP VERB: PUT*

**1.** 
- Verb: PUT
- URL is
```
http://localhost:5000/credits/<int:id>/
```
- You will be required to be authorized as an admin user in order to update credits. To login and provide authorization as admin, please refer to the instructions listed at the top of the R5 section. You will need to login as the admin musician, and then copy the access token provide, then paste it into the Authorization header as a bearer token.

- No fields are mandatory in the body as raw JSON data. Only the fields provided will be updated accordingly for credits. For example, if only the "description" field is provided, then the description of the credit will be updated only. 

Example where I updated the description of the credit_id = 3

Example URL used -> http://localhost:5000/credits/3

Example input data
```JSON
{
    "description": "Updated credit. I did the drums",
    "contribution_date": "1999-11-11"
}
```
Expected return data:
```JSON
{
    "credit": {
        "contribution_date": "1999-11-11",
        "description": "Updated credit. I did the drums",
        "id": 3,
        "musician_email": "mike@email.com",
        "musician_id": 3,
        "song_id": 5,
        "song_title": "Biking"
    },
    "message": "Credit updated successfully"
}
```


*DELETE ROUTE ENDPOINTS - HTTP VERB: DELETE*

**2.** 
- Verb: DELETE
- URL is
```
http://localhost:5000/credits/<int:id>/
```
- You will be required to be authorized as an admin user in order to delete credits. To login and provide authorization as admin, please refer to the instructions listed at the top of the R5 section. You will need to login as the admin musician, and then copy the access token provide, then paste it into the Authorization header as a bearer token.

- No fields are mandatory in the body as raw JSON data. Only need to provide URL indicating the credit_id to be deleted.

Example where I deleted credit_id = 6

Example URL used -> http://localhost:5000/credits/6

Expected return data:
```JSON
{
    "credit": {
        "contribution_date": "2014-12-11",
        "description": "Songwriting",
        "id": 6,
        "musician_email": "steve@email.com",
        "musician_id": 5,
        "song_id": 6,
        "song_title": "Thinkin Bout You"
    },
    "message": "Credit deleted successfully"
}
```

## R6

Below are the final ERD diagrams for this API Webserver application. 

![ERD](./docs/ERD_final.jpg)

![ERD](./docs/ERD_final2.jpg)

The third-party website Diagrams.net was used to create the ERD. 

It can be seen in this ERD that there are 4 relations: Musicians, Labels, Credits and Songs

Initially (as shown in R10), there were relations for Samples and Projects as well. After feedback from the instructors, I decided to remove these to reduce redudancy and complexity for the application. For future development of the application, a Samples relations can certainly be added (which represents any samples that were used in a song that need to be credited).
- Along with this, I found that the "Genre" column of the Songs relation could have been separated into it's own relation, thus further normalizing the database. However due to time constraints, I decided against doing this for the time being.
- The same could also be said for the "type" column of the Label relations. Another relation could have been created to further normalise the database, with the relation representing label "types" (such as Indepedent, Major etc.) Once again, due to time constraints I decided against doing this. 

Here is the database schema in written form, with the relations being capitalised:

LABELS (primary key: id, name, type)

MUSICIANS (primary key: id, first_name, last_name, profession, phone_number, email, password, admin, foreign key: label_id)

SONGS (primary key: id, title, genre, duration, date_finished)

CREDITS (primary key: id, description, contribution date, foreign key: song_id, foreign key: musician_id)

It can be seen that there is a one to many relationship between LABELS and MUSICIANS

- This relationship is implemented through the foreign key constraint in the MUSICIANS table which references the primary key of the LABELS table. Each musician can only be associated with only one label (a musician is not required to have a label). while each label can have multiple musicians associated with it (a label is not required to have musicians).

There is a many to many relationship between MUSICIANS and SONGS. A musician can have many songs, and a song can have many musicians. Due to this many to many relationship, a separate CREDITS relation was created to represent this.

There is a one to many relationship between MUSICIANS and CREDITS

- This relationship is implemented through a foreign key constraint in CREDITS table which references the primary key of MUSICIANS table. This means that each musician can have multiple credits associated with them, while each credit can be associated with only one musician.

There is a one to many relationship between SONGS and CREDITS

- This relationship is implemented through a foreign key constraint in CREDITS table which references the primary key of SONGS table. This means that each song can have multiple credits associated with it, while each credit can be associated with only one song.

All the above relationships are implemented using a foreign key constraint, which enforces data integrity and ensures that only valid data can be inserted into the database. In addition, the ERD also shows that each table has its own primary key, which uniquely identifies each record in the table.

## R7

Here are various third-party services that were used in this API webserver application:

1. Postman:

Postman is a standalone third-party API platform which is used to build, test, monitor and document APIs (Reference 11). Developers essentially use Postman to test HTTP verbs, where Postman's user-friendly Graphical Interface is an excellent tool for sending and viewing HTTP requests and responses. All the various type of HTTP requests such as GET, POST, PUT and DELETE can be made with Postman, with conversion between the API and code written in programming languages such as JavaScript, Python and JSON format is handled (Reference 10). Postman also offers a comprehensive set of tools to assist accelerate the API lifecycle - such as design, testing, documentation and mocking. It acts as an API repository where a developer team can collaborate and access the API on one central platform (Reference 10). Furthermore, Postman can help improve the qualities of APIs through setting governance rules ensuring that APIs are built, designed and tested meeting organisation standards (Reference 10). 

Postman was used as the third-party API platform of choice for this Webserver API Application, in order to test and monitor the API. 

2. PostgreSQL:

PostgreSQL is an open-source object-relational database management system (Reference 4). Due to it's widespread popularity in the industry, robust features, authentication and authorisation features available as well as the fact that use of PostgreSQL is free - PostgreSQL was used as the relational database management system of choice for this API Webserver Application.

3. Psycopg2:

Psycopg2 is considered the most widely used PostgreSQL database adapter for the Python programming language, allowing Python applications to communicate with the PostgreSQL database (Reference 12). It is an open-source third-party external software package.Psycopg2 was designed for applications that needed to perform various database operations, such as inserting, updating and deleting records from the tables in the database. Pyscopg2 is used to enable the execution fo SQL queries against the database, and retrieve the resutls of those queries (Reference 12).

Because PostgreSQL was used as the relational database of choice for the API webserver application, Psycopg2 was integral for the functioning of the application by facilitating interaction with PostgreSQL. 

4. autopep8:
autopep8 is a third-party Python package which automatically formats Python code to comply with the Pep 8 style guidelines (Reference 12). The reason this was used in the Webserver API Application was for convenience, as PEP 8 is the official style guide and convention for Python code. With the Webserver API Application being written in Python and using Flask, autopep8 helped automate the process of formatting Python code to conform to the PEP 8 style guidelines, thus helping save time and ensuring code consistency in the application (Reference 12).

5. Flask:
Flask is a third-party Python web framework. It provides tools and libraries to assist with developing web applications (Reference 13). Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template engine.

Flask is considered lightweight, flexible and easy to learn. Other advantages of using flask are that it's easy to set up. Flask has an intuitive API, and also provides a built-in development server - thus making it easy to test and debug applications (Reference 14).

It is also easy to add new functionality to applications through use of Flask extensions. There are various extensions available for Flask, which include extensions for database integration, authentication and API development (Reference 14). Flask is also compatible with many other Python libraries and tools. There is a large and active community around Flask, resulting a wide number of resources, documentation, tutorials and forums available for learning and troubleshooting (Reference 13). 

All these benefits reveal why Flask was a suitable choice for use in this API Webserver Application. 

6. Flask-SQLAlchemy:

SQLAlchemy is an ORM (Objet-Relational Mapping) library providing a simple interface for interaction with databases, through providing the full extensibility of SQL (Reference 8). The benefit of an ORM, especially SQLAlchemy, is that Python language can be used for database interactions and queries as opposed to having to use SQL. This offers more flexibility for applcations. Flask-SQLAlchemy is a third-party Flask extension that was installed, which adds support for SQLAlchemy. Flask-SQLAlchemy helps simplify the use of SQLAlchemy with Flask, through setting up common objects and patterns for using those objects (Reference 8). The use of SQLAlchemy was very important for the API Webserver Application, showing how the Flask-SQLAlchemy third-party extension was of great benefit. 

7. Marshmallow:

Marshmallow is a third-party ORM/ODM/framework-agnostic Python library (Reference 15). It is used for it's powerful serialisation and deserialisation capabiltiies, and for converting complex datatypes, such as objects, to and from JSON, native Python datatypes and other formats (Reference 15). In this application, Python objects could be converted to JSON strings, and incoming JSON data could be deserialised and converted back into Python objects. This is why Marshmallow was so useful in this application in the management of data within the Webserver Application (Reference 15). 

In this Webserver API Application, Marshmallow helped in the defining of the schemas for the data models, thus ensuring that the incoming data for the API was in the expected format and contained all the required fields (Reference 15).  This helped to prevent errors and maintain data integrity. SQLAlchemy is another third-party service that was used in the API Webserver Application. The benefit of using Marshmallow was that Marshmallow has great integration with SQLAlchemy, whhere SQLAlchemy model objects could easily be serialised and deserialised using Marshmallow (Reference 15). Once again, Marshmallow benefits include how it made the interaction with data and a database much easier for the APi Webserver Application. 

8. Marshmallow-SQLAlchemy:

As detailed in the above section, Marshmallow is easily integrated with SQLAlchemy. Marshmallow-SQLAlchemy is a third-party Marshmallow extension that was installed, which provided serialisation and deserialisation of SQLAlchemy database models to and from JSON and other formats. This was especially important in this Webserver API Application due to the extensive use of SQLAlchemy. 

9. Flask-Marshmallow:

As detailed in the documentation, Flask-Marshmallow is an integration layer for Flask and Marshmallow (Reference 16). It adds additional features to Marshmallow, including URL fields for APIs, as well as integrating with Flask-SQLAlchemy (Reference 16.) Flask-Marshmallow is a third-party extension that was used in this APi Webserver Application, due to its integration with both Flask and Marshmallow. 

10. Flask-Bcrypt:

Flask-Bcrypt is a third-party Flask extenstion which provides bcrypt hashing utilities for applications (Reference 12). As a password-hashing function, Flask-Bcrypt helps add an important layer of security for the API Webserver Application, by protecting sensitive data such as passwords (Reference 12). Flask-Bcrypt is great as well as it is easily integrated with Flask applications due to it being a Flask extension, thus making it simple to encrypt passwords and other sensitive data. 

11. Flask-JWT-Extended:

Flask-JWT-Extended is a third-party Flask extension that was used to add an authentication layer to the Webserver API Application. This extension provides support for JSON Web Tokens (JWTs) in Flask applcations, such as in the case for generating and verifying JWTs as well as token revocation and expiration (Reference 12). Flask-JWT-Extended is an important service that was utilised as authentication is another key component to creating security for the Webserver API application. JWTs can be used for authentication to protect routes and Flask-JWT-Extended simply made it easier for the application to work with JWTs (Reference 12).

12. VSCode:

Visual Studio Code (VSCode) is a source code editor that is available for Windows, macOS and Linux (Reference 17). It has a large number of extensions for programming languages such as Python. This is why VSCode was used as the code editor environment to write the code for this Flaks API Webserver Application.

13. Github:

Github is a website and cloud-based repository hosting service where developers and store, manage, track and control changes to their code (Reference 18). Github is used for Version control and Git. Github was used as a third-party service in development of this Flask Webserver API application, where the code was pushed to the repository provided by Github, to be stored and tracked. 

14. SQLAlchemy:

SQLAlchemy is a Python SQL toolkit and Object Relational mapper (Reference 8). It provides the functionalities and flexibilities of SQL, allowing efficient database interaction while being adapted into the Python programming language. Classes can be mapped to the database, which allows the object model and database schema to be developed through use of SQLAlchemy. SQLAlchemy is a third party service that was used for this API Webserver Application

15. datetime:

Datetime is a built in module in Python, which provides classes for working with dates and times. This allowed for functions to be developed in the application to ensure that the input data was correctly stored in time and date format in the database. 

## R8

The four relations in the database for the API Webserver application are: Labels, Credits, Musicians, Songs.

These database relations were represented in the application as Models (Label, Credit, Musician, Song). 

In this API Webserver Application, SQLAlchemy was used which is a Python SQL toolkit and Object-Relational Mapping (ORM library) (Reference 8). The benefit of using SQLAlchemy is that it allows Python classes to be defined, which represent database tables. These Python classes can then be used to interact with the database in a more Pythonic way. 

The 'db.Model' class is a base class provided by SQLAlchemy for creating Python classes which represent database tables. A set of attributes and methods are provided, which allows for the structure of the database tables to be defined. As an example, 'db.Column' can be used to define the columns of tables, and 'db.relationship' can define the relationships between tables.


**Label Model**

Below is the application code for the Label model, which represents the Labels relation in the database.

```Python
class Label(db.Model):
    __tablename__ = "labels"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=False)
```

It can be seen that the Label model is defined using the db.Model class, where the database table represented has the name "labels". There are three columns in the table, as shown by the db.Column class. 

- The first column is called id, and is the primary key for the table and stores an auto-incrementing integer value. 

- The second column is name, and stores a string value and is not able to be nullable meaning that a value must be provided for this column entry. 

- The last column is called type, and it also stores a string value and is not nullable.  

**Credit Model**

Below is the application code for the Credit model, which represents the Credits relation in the database. 

```Python
class Credit(db.Model):
    __tablename__ = "credits"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    contribution_date = db.Column(db.Date())

    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), nullable=False)
    musician_id = db.Column(db.Integer, db.ForeignKey(
        "musicians.id"), nullable=False)
```

It can be seen that the Credit model is defined using the db.Model class, where the database table represented has the name "credits". There are five columns in the table, as shown by the db.Column class. 

- The first column is called id, and is the primary key for the table and stores an auto-incrementing integer value. 

- The second column is description, and stores a string value and is not able to be nullable meaning that a value must be provided for this column entry. 

- The third column is contribution_date, and stores a date value. An entry for this column is not required.

- The last two column are song_id and musician_id and are both foreign key constraints. They both are not able to be nullable, meaning that a value must be provided for these two columns for the credits table. This is due to the fact that a credit cannot exist without a musician and song associated with it.

- These foreign keys highlight what is shown in the ERD for this application and database. There is a many to many relationship between musicians and songs. This resulted in the credits table having to be made. There is a one to many relationship between musicians and credits, where a credit must have one musician and a musician can have none or many credits associated. There is a one to many relationship between songs and credits, where a credit must have one song, and a song can have none or many credits associated.

- the song_id column as a foreign key in the credits table, references the primary key of the songs table. This is shown by ```db.ForeignKey("songs.id")``` where the id column of the songs table is referenced. 

- the musician_id column as a foreign key in the credits table, references the primary key of the musicians table. This is shown by ```db.ForeignKey("musicians.id")``` where the id column of the musicians table is referenced. 

The Credit model has foreign key relationships with both the Song and Musician models via the song_id and musician_id foreign keys. This allows for easy querying of credits for a given song or musician. A single credit belongs to only one song and only one musician, but each song and musician can have multiple credits.


**Musician Model**

Below is the application code for the Musician model, which represents the Musicians relation in the database.

```Python
class Musician(db.Model):
    __tablename__= "musicians"
    
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    profession = db.Column(db.String(), nullable=False)
    phone_number = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    label_id = db.Column(db.Integer, db.ForeignKey("labels.id"), default=None)

    credits = db.relationship(
        "Credit",
        backref="musician",
        cascade="all, delete"
    )
```

It can be seen that the Musician model is defined using the db.Model class, where the database table represented has the name "musicians". There are nine columns in the table, as shown by the db.Column class. 

- The first column is called id, and is the primary key for the table and stores an auto-incrementing integer value. 

- The next columns are first_name, last_name, profession, phone_number, email and password. These columns store string values are not able to be nullable meaning that a value must be provided for this column entry. 

- The email column also has a unique=True attribute meaning that any email entries into the database for the musicians table must be unique. 

- The next column is admin and this stores a boolean value where the default is False. Only musicians who have this admin column entry as True, are able to act as admin users in the database. 

- The last column is label_id. This has a default as None, due to the fact that not every musician has to be associated with a label, hence they will need to provide a label_id when registering if they are associated with one. label_id is a foreign key constraint which references the "labels" table's primary key which is called "id", as shown by ```db.ForeignKey("labels.id")```. This column stores an integer value. This label_id field in the Musician model as a foreign key referencing the id field in the Label model, represents the relationship between the two models. A single musician can only have one associated label, whereas each label can have multiple associated musicians - showing the one-to-many relationship between Muscian and Label. 

Another aspect to note in the model is this specific section of code

```Python
credits = db.relationship(
        "Credit",
        backref="musician",
        cascade="all, delete"
    )
```
db.relationship is an attibute used to define a relationship between two tables. In this case, a one-to-many relationship is defined between the Credit and Musician models. Each credit is associated with one musician, and each musician can have multiple credits. This was also explained previously, where the Credit model itself has the foreign key "musician_id" which references the primary key "id" column of the Musician model. 

The backref attribute is used to create a bi-directional relationship betwen two tables/models - credits and musicians. This allows birectional querying. With the setting backref="musician" in the Credit model, SQLAlchemy automatically creates a credits attribute on the Musician model, which allows you to access all of the credits associated with a particular musician through musician.credits. 

The cascade attribute is used to specify how changes to one table should be propagated to related tables. In this example, cascade="all, delete", meaning that if a musician is deleted, all of their associated credits should also be deleted. This is useful to ensure that the database remains consistent with no orphaned records that are no longer associated with anything - further highlighting how a credit must be associated with one musician. 

**Song Model**

Below is the application code for the Song model, which represents the Songs relation in the database.

```Python
class Song(db.Model):
    __tablename__= "songs"

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(), nullable=False)
    genre = db.Column(db.String(), nullable=False)
    duration = db.Column(db.Time())
    date_finished = db.Column(db.Date())

    credits = db.relationship(
        "Credit",
        backref="song",
        cascade="all, delete"
    )
```

It can be seen that the Song model is defined using the db.Model class, where the database table represented has the name "songs". There are five columns in the table, as shown by the db.Column class. 

- The first column is called id, and is the primary key for the table and stores an auto-incrementing integer value. 

- The second column is title, and stores a string value and is not able to be nullable meaning that a value must be provided for this column entry. 

- The third column is genre, and stores a string value and is not able to be nullable meaning that a value must be provided for this column entry. 

- The fourth column is duration and stores a time value. It is able to be nullable which means a value isn't necessary for this column entry.

- The last column is called date_finished, and it stores a a date value, and is also able to be nullable which means a value isn't necessary for this column entry.

Another aspect to note in the model is this specific section of code:

```Python
credits = db.relationship(
        "Credit",
        backref="song",
        cascade="all, delete"
    )
```
db.relationship is an attibute used to define a relationship between two tables. In this case, a one-to-many relationship is defined between the Credit and Song models. Each credit is associated with one song, and each song can have multiple credits. This was also explained previously, where the Credit model itself has the foreign key "song_id" which references the primary key "id" column of Song model. 

The backref attribute is used to create a bi-directional relationship between two tables/models - credits and songs. This allows birectional querying. With the setting backref="song" in the Credit model, SQLAlchemy automatically creates a credits attribute on the Song model, which allows you to access all of the credits associated with a particular song through song.credits. 

The cascade attribute is used to specify how changes to one table should be propagated to related tables. In this example, cascade="all, delete", meaning that if a song is deleted, all of their associated credits should also be deleted. This is useful to ensure that the database remains consistent with no orphaned records that are no longer associated with anything - further highlighting how a credit must be associated with one song. 

The relationships shown between all the models allow for the efficient querying of data based on the associations between them. All of this is done through the use of foreign keys as well as the db.relationship function. For example, you can easily find all credits for a given song by accessing the credits field of that song, or you can find all songs credited to a given musician by accessing the credits field of that musician and then accessing the song field of each credit.

The models in the application also make use of appropriate model methods for querying on self and its relationships. For example, you can use the query method of the Song model to retrieve all songs, the filter_by method of the Song model to filter songs based on a specific condition, and the join method of the Credit model to join the Song and Musician tables to retrieve all songs credited to a given musician.


## R9

The four main database relations that were implemented in the application are as follows:
- Labels
- Musicians
- Credits
- Songs


**Labels**

The main purpose of this API Webserver application is to track the credits and contributions that musicians have made on songs. Labels represent Record Labels, as many musicians are associated with labels (this is also relevant as when things such as financial distribution of song royalties are decided, whether a musician is associated with a label will affect this as well). 

In terms of the Labels relation, there are three columns which are the id as the primary key, the name of the label which is stored as a string, and the type of label which is also in string format. The id for this relation is an auto-incrementing integer value. The id as the primary key is to uniquely identify each entry in the Labels relation. 

There were considerations to include further columns such as label contact phone number, as well as country that the label is from, however these were decided not to be included to reduce complexity. Furthermore, the minimum viable product for the application is mainly focussed on the credits, songs and musicians. The label name would be things such as "Warner Records" and "Sony Records". The label type would represent things such as whether the Label is "Major" or "Independent". 

As mentioned previously, it was up for consideration whether to separate the Label "type" into it's own relation, thus further normalising the table. This relation would store all the types of labels. However once again to reduce complexity of the application for it's initial development, this was route was not taken. 

**Musicians**

The next database relation was for Musicians. For this particular API Webserver Application, Musicians represented the "users" of the application, where musicians could register, login and add their credits to songs. The columns for the Musicians relation are as follows:
- id (Primary key)
- first_name 
- last_name 
- profession
- phone_number
- email
- password
- admin
- label_id (Foreign key)

The id column representing the Primary key of the Musicians relation is formatted as an auto-incrementing integer value. The primary key is in place to uniquely identify each entry in the Musicians relation. The admin column is stored as a boolean value. This is important for the application as only Musicians who had an admin value as "true" were able to execute queries such as deleting and updating other relations. This is a further layer of security to prevent other musician users being able to delete other musicians and damage the database structure. 

**Musician to Label relationship**

The label_id column is a foreign key constraint in the Musicians table, which references the primary ky of the Labels table. 

- This is because there is a One-to-many relationship between Labels and Musicians. 

Each musician can only be associated with one label, while each label can have multiple musicians associated with it. The relationship isn't mandatory on both ends, as a musician can be added to the database without having a label (representing a real world scenario as not all musicians are associated with a label), and a label can be added to the database without being associated with musicians. The structure of the database in the application was implemented with this relationship in mind. 

All other columns in the Musicians relation were stored as string values. Initially, phone_number was stored as an integer value, however after some research it was found that it was best to store phone_number as a string value as not all phone numbers contain only integers. The profession column would represent the professions of the musicians, which includes things such as singer, songwriter, engineer, producer, guitarist, drummer etc. As each musician was essentially a "user" within the application that could register and login, a password column was included (this was encrypted in the application through Flask-Bcrypt). When a musician logged in to the application, they would provide their email address and password in order to receive their access token. 

The name of the musician was stored in separate columns first_name and last_name so that it'd be easier to search for musicians in the future. Other columns such as phone_number and email were important to include to record the musician's contact details. 

In order to register a musician in the application, the columns first_name, last_name, profession, phone_number, email and password were required to be provided - therefore not nullable. The admin column could only be changed by only other musicians users who were admins. The label_id was not required to be provided, where the default was None, as not all musicians are associated with labels. If a label was deleted from the database, and the musician had a foreign key in it's table that referenced the deleted label, then once the label was deleted the column would simply be set to None. 

**Songs**

The next database relation is Songs. The columns for the Songs relation are:
- id (Primary key)
- genre
- duration
- date_finished

id is once again an auto-incrementing integer value that represented the primary key to uniquely identify each row in the Songs relation. Genre is stored as a string value, representing a song's genre (such as RNB, Rap, Pop, Country etc). Duration represented how long a song was, and was stored as a time value HH:MM:SS (e.g. 00:03:20). Date_finished represents the date the song was finished, and was stored as a time value YYYY-MM-DD (e.g. 2023-03-01).

When creating a new Songs relation entry in the database, the mandatory fields were title and genre. Duration and date_finished were not mandatory to include. 

Other ideas for columns in the Songs relation included BPM, Key signature etc. However due to time constraints for a minimum viable product, these were not included. The main function of the app is ensure that a song is properly identified (via it's name, genre and id), and the credits that are associated with the song. 

There was also the idea to further normalise the Songs relation and have the column "genre" separated as it's own Genre relation. This relation would store all the possible genres in the database. However due to time constraints and keeping things simple for the MVP of the application, this was not implemented. 

**Relationship between Songs and Musicians**

There is a many-to-many relationship between Songs and Musicians relations. It was implemented so that one song could have many musicians associated with it, and one musician could have many songs associated with them. Because of this many-to-many relationship between Songs and Musicians, a separate Credits relation was required to be created. 

**Credits**

The last database relation is Credits. The columns for the Credits relation are:
- id (Primary key)
- description
- contribution_date
- song_id (foreign key)
- musician_id (foreign key)

The id column for the Credits relation is an auto-incrementing integer value, that represents the primary key to uniquely identify each row in the Credits relation. Description is stored as a string value, and represents the Musician's credit for a song e.g. played drums, sung vocals, wrote the lyrics etc. The contribution_date represents the date that the Musician made the contribution to the song, and is stored as a date value YYYY-MM-DD (e.g. 2023-03-01).

The Credits table has two foreign key constraints. The song_id column references the primary key (id) of the Songs relation, and the musician_id column references the primary key (id) of the Musicians relation. 

The song_id and musician_id columns are mandatory required fields for the Credits table, as a Credit cannot exist without a musician or song associated with it. 

**Relationship between Credits and Musicians**

There is a one-to-many relationship between the Musicians and Credits relations. 

This relationship is implemented through a foreign key constraint in CREDITS table which references the primary key of MUSICIANS table. This means that each musician can have multiple credits associated with them, while each credit can be associated with only one musician.

It is mandatory that a credit has to be associated with a musician, however it is not mandatory for a musician to be associated with a credit. If a musician was deleted from the database, it's associated credits would also be deleted. A credit being deleted from the database would not delete the associated musician. 

**Relationship between Credits and Songs**

There is a one-to-many relationship between the Songs and Credits relations. 

This relationship is implemented through a foreign key constraint in CREDITS table which references the primary key of SONGS table. This means that each song can have multiple credits associated with it, while each credit can be associated with only one song.

It is mandatory that a credit has to be associated with a song, however it is not mandatory for a song to be associated with a credit. If a song was deleted from the database, it's associated credits would also be deleted. A credit being deleted from the database would not delete the associated song. 

**Overview of relationships**

The three main relationships were:

1. A one-to-many relationship between Labels and Musicians

And because of the many-to-many relationship between Musicians and Songs, the separate Credits relation was created.

2. A one-to-many relationship between Musicians and Credits
3. A one-to-many relationship between Songs and Credits. 

These relationships are shown in the ERD. 

A song can have many credits, and a credit can belong to only one song and one musician.
A musician can have many credits, and a credit can belong to only one song and one musician.
A label can have many musicians, and a musician can belong to only one label.

All the relationships between the database relations were implemented using a foreign key constraint, which enforces data integrity and ensures that only valid data can be inserted into the database. In addition, the ERD also shows that each table (relation) has its own primary key, which uniquely identifies each record in the table.

*This is also the relational model in written form:*

LABELS (primary key: id, name, type)

MUSICIANS (primary key: id, first_name, last_name, profession, phone_number, email, password, admin, foreign key: label_id)

SONGS (primary key: id, title, genre, duration, date_finished)

CREDITS (primary key: id, description, contribution date, foreign key: song_id, foreign key: musician_id)

## R10

# Shows significant planning for how tasks are planned and tracked, including a full description of the process and of the tools used
# Describe the way tasks are allocated and tracked in your project#

1. __Initial set up__

Upon starting the API Webserver Project, the service Trello was used as the digital Kanban board for the project. Tasks were created, allocated and tracked using Trello. Time deadlines in terms of priority allocation was also a feature utilised for each of the cards created on the Trello Board - each card representing a task to be completed. Any ideas and notes were also commented and recorded on the Trello cards.

This is the link to the Trello Board for the project - https://trello.com/invite/b/LKKBjbPd/ATTI6453a42b8281317a5030cb78578f7cad0577A38A/webserver-api-assignment


Agile methodology was used to help with the development of this project. All the tasks in this API Webserver application were broken into smaller tasks. Though because this project was coded in an educational environment as opposed in the industry, the traditional approach of using 2 week sprint cycles was not used. Instead, the concept of daily standups were used. Where at the start of each day there would be a review of the tasks that were completed, and the ones that needed to be completed. With these regular review intervals, the completion and development for the Application was able to be kept on track and managed.

The first step of the project was the brainstorming of ideas for the API Webserver application. A user-centric approach was taken to ensure the usefulness of the API webserver application to solve the intended problem. The initial requirements of the project were - to settle on an idea, create an ERD for the database, get the idea approved by the instructors and note any features that needed to be implemented for the project. Trello was used, where a cards on the Kanban Board were useful for commenting all the ideas and tasks that were part of the brainstorm and planning. 

Once all the requirements of the project were defined, all the smaller manageable tasks of the project were broken down. Cards were created using the Trello Kanban board, with each card representing a task to be completed for the Webserver API application. Trello allowed for easy visualisation to see all the tasks that needed to be completed, and had already been completed.

A To Do, and Backlog/Initial project discussion columns were created to store all the tasks that needed to be completed but had not yet been started on. An In-progress column was created on the Trello board to store the list of tasks that were currently being worked on for the day (a day representing a very small sprint cycle). A done column was also implemented to contain the list of tasks that had already been completed. This allowed for easy visualisation of what tasks were already down, and also made it easy to revisit any previously completed tasks. The approach of making and prioritising tasks was based on esnuring the essential features of the application and project were to be completed - ensuring a minimum viable product of the project to be done. These would include the coding of the application as well as the requirements documentation of the project. Each task also represented a specific feature or functioality of the application - such as the commands file to create, seed and drop the database tables, the schemas files, the models files and the controller files. Separate tasks were also created for each specific documentation requirement - e.g. documentation of the API endpoints, explanation of the ERD, explanation of the chosen database system etc. 

As stated before, daily standups were held for reflection and review of the previous day's work as well as to refresh on what tasks needed to completed for the project. This included opening the Trello Board and reviewing what tasks were in progress, and what tasks were already completed.  

Below is a screenshot of the initial Trello board that was set up, including the tasks that were created and moved to In progress or Done. 

![Trello Screenshot](./docs/Trello_1.jpg)

Trello was used previously for the T1A3 Terminal Assignment, and the board used for this assignment was duplicated for the T2A3 API Webserver Project as well. However, there were a few changes made. 

Firstly, I changed the column 'Pending' to 'In progress'. I found in the previous project that a pending column wasn't utilised as it implied that the task was moved to this column to be approved by another Team or was delayed due to timing. I came to find that this was not necessary for this project as I was the only Team member. Instead, I renamed the column to 'In progress' which suited better for this project's needs.

I also split the 'Done' column into two columns which were Tasks Done and Coding Done. I found this easier to track the overall tasks for the project that were completed. This way I could see which tasks were done, which were not coding related such as research, and which coding specific tasks were completed - rather than having it all in one column. 

In the initial set up of the project, the first tasks that were the main priority was to brainstorm and finalise the idea for the API, and then complete the ERD diagram for the database of this API. 

I had used a Trello card to record any ideas that I came up with for the API project. Eventually, I settled on the idea to track collaborators for song credits.

In terms of creating the ERD diagram, I utilised the service https://diagrams.net/. 

Below are screenshots of the initial ERD diagram that was created prior to feedback and approval from the instructors.

![ERD](./docs/ERD_1.jpg)

![ERD](./docs/ERD_2.jpg)

2. __Second phase__

After gaining approval from the instructors, I created tasks for each of the Requirements/Rubrics that were not coding related. I felt that I could complete these first as quickly as possible. 

These tasks included explaining the reason for the API project and problem it was solving, research on ORMs and on the database management system chosen for the project. 

Below is a screenshot of how the Trello Board looked at this time:

![Trello Screenshot](./docs/Trello_2.jpg)

3. __Third phase__

I completed the initial tasks that didn't rely on any coding or the database schema to be set up/finalised.

After this, I had made edits to the ERD according to the instructor feedback. The main points of feedback were that the projects table was not necessary as musicians were already related to the songs table through the credits table. Also, the sample & sample_use tables were valid however using these would add unnecessary complexity for this stage of the process. Hence I made the decision to remove this.

I did have the idea to further normalise the Songs table by making a separate "Genres" tables. However, for now I decided to not do this to reduce complexity. If time would allow for it, I would possibly do this later in the project. 

Here is what the adjusted ERD looked like at this time:

![ERD](./docs/ERD_3.jpg)

Aside from removing the Sample, Sample_Use and Projects table, I added the column "duration" to the Songs table to be able to query by song duration in the future.

The next priority after this was moving onto the coding of the application. The first tasks I prioritised was to ensure that the ERD was properly translated so that the database schema was set up and working as intended.

This is so that I could check that the database schema didn't have any issues, before completing any coding related to querying that databse through the coding of controllers.

Here is what the Trello Board looked like at this time:

![Trello Screenshot](./docs/Trello_3.jpg)

4. __Fourth phase__

The following coding-related tasks were completed at this time:

- Initial set up on the application
- Installing all requirements + setting up database/user in PostgreSQL
- Initial main.py file created along with config.py file
- Database ERD Schema has been implemented. The models and controllers python files have been completed
- Commands.py file created. Tables were able to be created and dropped. Data has also been added to be seeded into all of the tables.

With the initial application set up complete and most coding related to the database creation and seeding complete - it was time to start on the API related aspects of the application.

I created a number of tasks related to specifically the controllers of the application, which would house the code for the HTTP verbs and API endpoints.

Here is the Trello Board at this point for this phase:

![Trello Screenshot](./docs/Trello_4.jpg)

It can be seen that I had made a whole new column called "Testing done". This is because I realised that there would be a lot of testing of the application and API endpoints. Hence I believed it would be best to split the coding and the testing related tasks.


5. __Fifth phase__

At this time, 90-100% of the coding had been completed for the application. The only coding left was adjustments to account for errors and testing. 

As code was completed, the testing related tasks were completed accordingly (for example, tests related to the associated functions of code that were written). API testing to ensure that everything was working as intended, was completed throughout the coding process.

This can be shown in the Trello Board screenshot below at this time:

![Trello Screenshot](./docs/Trello_5.jpg)

For this phase, it was noted that the next tasks to complete was all the documentation related tasks that could be addressed once most of the coding was done.

This included
- Detailing all API endpoints
- Explaining ERD, relations and models
- Explaining third party services/packages used. 

During this time, I also made a number of edits to the ERD diagram to accurately reflect what was coded in the API Webserver Application. 

6. __Final phase__

At this point in time, R5 of the documentation was completed detailing the APi endpoints. 

I had made the decision to test all the APi endpoints and queries whilst documenting them. This helped me to make sure everything was working as intended, whilst completing the documentation.

After this, the documentation for the ERD, database Relations, application Models and explanation of the third party services/packages were completed.

Once again, whilst documenting these, specifically for the Models, I also did a review of the code for the Models and Schemas. This was done to help save time by batching these tasks together. 

After all the documentation was done, the final tasks to complete was to review the comments in the application code to ensure that everything was clear, as well as completing the final R10 documentation showing the planning of tasks for this project. Here is the final screenshot of the Trello board at this time:


![Trello Screenshot](./docs/Trello_6.jpg)


## REFERENCES

(1) [AWS](https://aws.amazon.com/rds/postgresql/what-is-postgresql/)

(2) [LinkedIn](https://www.linkedin.com/pulse/what-postgresql-introduction-advantages-disadvantages-ankita-sharda/)

(3) [Guru99](https://www.guru99.com/introduction-postgresql.html)

(4) [PostgreSQL](https://www.postgresql.org/about/)

(5) [Ed](https://edstem.org/au/courses/10081/lessons/27619/slides/195155)

(6) [freeCodeCamp](https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/)

(7) [FullStackPython](https://www.fullstackpython.com/object-relational-mappers-orms.html#:~:text=Why%20are%20ORMs%20useful%3F,and%20schemas%20in%20their%20database.)

(8) [SQLAlchemy](https://www.sqlalchemy.org/)

(9) [Bits and Pieces](https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a)

(10) [Postman](https://www.postman.com/)

(11) [javatpoint](https://www.javatpoint.com/postman)

(12) [Pypi.org](https://pypi.org/)

(13) [Pythonbasics](https://pythonbasics.org/what-is-flask-python/)

(14) [Flask](https://flask.palletsprojects.com/en/2.2.x/)

(15) [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)

(16) [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)

(17) [Vscode](https://code.visualstudio.com/docs)

(18) [Github](https://github.com/)










