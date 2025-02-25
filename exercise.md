# Introduction

Hello!

Thank you for your interest in the Lead Backend engineer role at [Moxie](https://www.joinmoxie.com/). We think that we’re building something very special and we’re excited about the idea that you might join us for the ride!

## Goals

The goal of this take-home assignment is to help us assess your ability to:

1. Design sensible, robust database table schemas
2. Write RESTful CRUD functionality for the given tables

A few notes before we dive into it:

### Time commitment

While we can discuss the topic of this assignment for many hours, we think that you should limit the amount of time you spend on it to *two hours maximum*.

### Missing context & Questions

<aside>
💡 Please ask questions as they come up! You can do so by [adding comments to this page](https://www.notion.so/help/comments-mentions-and-reminders)

</aside>

*This document does not include all of the contextual information that you need to complete the assignment.* Some of that is due to the fact that we’re not exceptionally good at writing take-home exercises, and some of that is intentional. 

In short, *this test will ask you to make assumptions and guesses about how to fill those gaps*. When you feel like you have to do so, use common sense and exercise your best judgment and if you have the time, document your reasoning.

# Exercise

## Context

At Moxie, each medspa defines a menu of services that customers can select when booking an appointment. You can see an example here in our online booking flow:

- note how a customer can select one or multiple services, each with a different name, length of time, and pricing.

<aside>
💡

Please review the example screenshot carefully: it provides some additional context on the data model what the API will need to be able to support

</aside>

![Screenshot 2024-01-30 at 14.07.20.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/691ad6c1-489f-4e57-a0e3-e2da905006db/cce27330-0baf-493d-bb33-fdd342a9f5f8/Screenshot_2024-01-30_at_14.07.20.png)

### What is the problem?

We need to create a simple CRUD app that allows customers to select services and book appointments for a given medspa - that means implementing a data model and RESTful endpoints that can create, update, list, and retrieve those records.

*What are Moxie’s products and services?*

Services are medical and non medical treatments administered by our providers (ie nurses). Any service will have several components

- a service category - ie injectables, peels, threads, etc
    - a service type - for example the injectables category includes several types of injectables such as neuromodulators, HA dermal filler, and Calcium Hydroxyapatite
        - a service product - types can have up to multiple products. For example botox, daxxify, and xeomin are all neuromodulator products.
        - an optional supplier - some products are produced by a specific vendor, who may make multiple product lines across multiple service types and/or service categories.

Please use the following [limited list of official services](https://docs.google.com/spreadsheets/d/1s6NPs7HQKmDZb_AFyw-vR-2pBKxrtuIeFpWvd2UtqmU/edit#gid=0) (google sheets link) that medspas can offer in the US (neuromodulators, chemical peel, HA dermal filler, etc).  Your data modeling should support the structure laid out in the speadsheet. 

### How do we want to solve it?

We’d like to solve that by:

1. We want to implement a data model to represent a medspa, it’s service(s), and its appointment(s), which can use one or more of those service(s)
2. We also want to implement a RESTful CRUD API that allows us to create, retrieve, and update medspa service(s) and appointment(s) records. 

## Assignment

<aside>
💡 Important! Please remember that Moxie uses Postgres for all of our database and reporting use cases.  As such, if you are writing non Postgres SQL, please be sure to annotate and explain any language specific elements of your schema design (ie MySQL, SQL Server, Oracle DB, etc)

</aside>

### Prompts

1. Design a data schema to support the following: 
    1. A medspa has the following properties
        1. id
        2. name
        3. address
        4. phone number
        5. email address
    2. A appointment has the following properties
        1. id
        2. start_time
        3. total_duration - derived from sum of all related service’s `duration`s
        4. total_price - derived from the sum of all related service’s `price`s
        5. status, which can be one of
            1. scheduled
            2. completed
            3. canceled
    3. A service has the following properties
        1. id
        2. name
        3. description
        4. price
        5. duration
    4. a medspa can have many appointments
    5. an appointment is related to a single medspa
    6. a medspa can have many `service`s
    7. a service is related to a single medspa
    8. an appointment can have many `service`s
    9. a service can be related to many `appointment`s
2. Implement a simple RESTful CRUD app that does the following:
    
    <aside>
    💡 *IMPORTANT NOTE ON TIME:* if you don’t have enough time to set up a setup and connect a database to your app, please feel free to use JSON files instead (ie you can read from and write to a JSON file and use it as a pseudo database for your application.
    
    </aside>
    

1. *SERVICE CRUD*
    1. allows an API consumer to create a service record
        1. when creating a service it is a requirement to specific which medspa it is associated with.
    2. allows an API consumer to update a service record, specifically it’s name, description, price, and duration.
    3. allows an API consumer to retrieve a service by its id
    4. allows an API consumer to retrieve a list of all services for a given medspa.
2. *APPOINTMENT CRUD*
    1. allows an API consumer to create an appointment record.  
        1. as part of this create call, I should also be able to specifiy one or more services to be associated with the appointment.
        2. example: 
            1. say that the given medspa has 3 services: botox, daxxify, and xeomin
            2. when creating the appointment I should be able to pass those three services, with the expectation that appointment’s total_duration and total_price is derived from those related services.
    2. allows an API consumer to retrieve a specific appointment by it’s id
    3. allows an API consumer to update an appointment’s status (ie from scheduled -> completed, or scheduled -> canceled
    4. allows an API consumer to list all `appointment`s
        1. if you have time, an extra goal would be to allow for retrieving all `appointment`s of a given status
        2. if you have time, an extra goal would be to allow for retrieving all `appointment`s of a given start_date (notice we say “date” here and not time)
1. Once created, please upload application to github and include a link for us to review it below
    1. please also include a readme with instructions on how to run your application and with some examples of calls we can make to your API. 

Please add your answers to this page in the section below. For step 1, please provide a set of production-ready “CREATE TABLE” statements describing the tables you would create. (Optionally, you can also add a visual representation of the tables and their relationships, but it’s not required.)

---

# Candidate submission below

<aside>
💡 Hey! You’re in the right place. please add all of your work in the section below, and thank you for the time and work, we appreciate it.

</aside>

---

<aside>
💡 If you wan to make a code snippet, you can use “” for a single line code block or “``” for a multi-line block (the multi-line block also allows you to define the language formatting to use (ie javascript, python, SQL, etc)

To upload a file, you just need to type in “/file”

</aside>