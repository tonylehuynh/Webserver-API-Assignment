# TONY LE HUYNH - GCAB012201 - WEB SERVER API ASSIGNMENT

## _R1_ 

The problem being solved by this application is that of tracking song credits - in particular the collaborators on songs. 

Despite typically seeing only one artist's name tied to songs, the majority of songs have multiple collaborators. There are many pop songs that have multiple songwriters. Along with this are producers and instrumentalists that collaborate to bring a song idea to life. Typically there will also be a vocalist, a singer or rapper, on a track who will be recorded by a recording engineer. Once everything has been recorded, the song will typically be mixed by a mixing engineer and then mastered by a different mastering engineer. 

This shows that there are many people that are involved with seeing a song come to life, before the song even reaches the ears of the public. This also means that there are many people who will need to be included on the song's credits list, and also compensated accordingly in the form of fees or royalties. 

As it can be difficult to keep track of all collaborators who were involved in a song, this particular API Web Server application will be of assistance. Users can register themselves as musicians, classified by the type of musician they are such a drummer or vocalist, and then record their contribution to a song. This application will help track all the collaborators on a song. Furthermore, a lot of musicians are associated with record labels (which adds to further complexity in terms of the splitting of payments as there can be many people such as lawyers and publicists on a label team), which is why record labels that musicians are associated with can be tracked on this application too. 

## _R2_

The reasons this particular problem of tracking song credits needs solving, is due to both fairness and legality. 

It is simply the right and fair thing to do when properly crediting those who have contributed to a song, or any project in particular. This is so that people are properly acknowledged and credited for their hard work. Also, being credited is very important for peoples' careers as this can help people find other work as well. 

Furthermore, the music industry is built on trust and relationships. Artists collaborate with each other in good faith. If someone does not get fairly credited for their work, this can damage professional relationships as well as industry reputation. The musician will no longer want to work with the artist. Word can also spread in the industry, which can damage the artist's reputation and their future possibilities of having other collaborators work with them. Not only this, but if word spreads to the public then the artist's public reputation can also be damaged as well. Overall, it is important that all collaborators on songs are properly acknowledged and credited to preserve trust and relationships that have been built. 

Another issue is the legality when it comes to crediting collaborators. Artists' and record labels have a legal obligation to credit and properly compensate collaborators.

As mentioned before, there are many collaborators who are typically involved with the making of a song. These include people such as songwriters, instrumentalists (drummer, bassist, guitarist, pianist etc.), producers, vocalists (singers & rappers), recording engineers, mixing engineers and mastering engineers. 

Depending on the business arrangement, each collaborator will have their own fee or will be entitled to a percentage royalty of the song. Once a song has been completed and submitted to be released to the public, collaborators will need to be compensated accordingly. 

Failure to properly financially compensate collaborators can result in legal issues for the artist, their team and their record label. Legal disputes can be very time consuming and result in heavy costs due to legal fees. Therefore, it is important that this issue is avoided altogether. 

Overall, it is important to keep track of collaborators in the making of songs in order to properly credit them both in writing and financially. The reason I have all this information is due to the fact that I've worked in the music industry myself and also have many friends in the music industry. 

The making of a song can take months, let alone years for some songs. Many artists also travel or work online by sending files, resulting in collaborators potentially being from all across the world. In this time, things can become lost or forgotten. With the large amount of collaborators on songs, it can be very difficult to keep track of who worked on a song and what their contribution was. 

This is why these problems presented above, can be addressed through the building of this API Webserver Project - where the collaborators/credits for the song making process will tracked and recorded. 

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

An ORM such as SQLAlchemy can allow the structure of a database schema to be defined in the code of the application itself. This is a benefit as it the approach is more intuitive and flexible than writing raw SQL queries. For example with SQLAlchemy, tables and columns in the database schema can be defined as Python classes and attributes. This also makes it more convenient and easier to maintain the database, and make changes to the schema without having to directly modify the database (Reference 6).

_Data Persistence_

ORMs make it easier to persist data to the database, such as creating tables, seeding the tables with data and executing SQL queries. Developers are able to perform CRUD (Create, Read, Update, Delete) operations on the database through use of an ORM (Reference 7). Tables n a database are able to be created, modified and deleted through use of an ORM as well. 

_Querying_

A key functionality of an ORM such as SQLAlchemy, is that database queries are able to be written in the programming language of the application, such as Python, rather than writing SQL queries. Python code can be written for an application, and the ORM will generate the corresponding SQL queries and execute them and interact with the database(Reference 6). SQLAlchemy provides a database abstraction layer that allows developers to interact with databases using an object-oriented approach. Another way to describe this is that SQLAlchemy provides a SQL Expression Language, allowing complex SQL queries to be written using a Pythonic syntax. 

ORMs such as SQLAlchemy also provide advanced querying capabilities. This includes tasks such as filtering, sorting and grouping data, as well as complex joins and subqueries (Reference 8). 

When interacting with databases, ORMs such as SQLAlchemy also utilise a method called connection pooling. This is where existing database connections are reused rather than creating a new one, thus helping improve the performance and efficiency of applications interacting with database systems (Reference 8). 

Overall, it is easier to read and write queries that interact with the relational database through use of an ORM. ORMs abstract the details of database operations, including the generation of SQL queries, executing them, and parsing the results. 

_Relationships_

An important aspect of relational databases are the relationships between tables in the database. An ORM provide a convenient way for these relationships between tables in the database to be defined and managed, which is especially important for data models with many-to-many or one-to-many relationships. ORMs allow you to define relationships between classes by defining attributes that reference other classes (Reference 7). 

In particular with SQLAlchemy, database tables can be defined using Python classes and attributes, along with the relationships that tables can have between each other through the use of features such as primary and foreign keys (Reference 7).

_Migrations_

Database migrations can also be managed by ORMs, where the modification of the schema of a database over time without losing data is made easier. This is where code written in a programming language, such as Python in the example of using SQLAlchemy, can be written to make changes to the database schema and then executed to apply the changes to the overall database. ORMs can ensure that the integrity of the database is maintained and that data is not lost during the modifications made to the database schema (Reference 6).

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

An ORM can help optimise database queries and the number of database connections, through the use of methods such as connnection pooling (Reference 6). Thus, the performance application and load on the database server are improved and therefore the scalability of applications can be optimised through using ORMs. 

_Testing_

The use of an ORM can make it easier to write and execute tests. This is because code written in an application using an ORM can be tested without having to interact with the database (Reference 6). 


## R5

dasds

## R6

dasds

## R7

dasds

## R8

dasds

## R9

dasds

## R10

# Shows significant planning for how tasks are planned and tracked, including a full description of the process and of the tools used
# Describe the way tasks are allocated and tracked in your project#

1. __Initial set up__

Upon starting the API Webserver Project, the service Trello was used as the digital Kanban board for the project. Tasks were created, allocated and tracked using Trello. Time deadlines in terms of priority allocation was also a feature utilised for each of the cards created on the Trello Board - each card representing a task to be completed. Any ideas and notes were also commented and recorded on the Trello cards.

This is the link to the Trello Board for the project - https://trello.com/invite/b/LKKBjbPd/ATTI6453a42b8281317a5030cb78578f7cad0577A38A/webserver-api-assignment


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

2. __Third phase__

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







