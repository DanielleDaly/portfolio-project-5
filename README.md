# Books Bazaar E-Commerce Store
## Milestone Project 5
The aim of this project is to build a full-stack web application using Django (the full-stack Python framework), HTML, CSS and JavaScript.
- This e-commerce web application is a fictional online book store.
- The functionality included in this web application includes, but is not limited to
    - An e-commerce store
    - Payments with [Stripe](https://stripe.com)
    - A book reviews area
    - A contact form for customer enquiries
    - Confirmation emails being sent to the user
    - CRUD functionality for the application admin users to manage products
    - An admin area for application admin users to manage book reviews, orders, users and view customer enquiries
        - I have included admin credentials in the project submission for assessors to log in
- This web application was built for educational purposes and no orders that are placed will be fulfilled.
- The Stripe payments implementation is set up for testing purposes only. No payments will be taken from users' accounts and users should not input their real debit or credit card details.
    - For completing purchases the below credit card details should be used:
        - Card number: 4242 4242 4242 4242 or 4000 0025 0000 3155 (Will prompt for purchase verification)
        - Any date in the future
        - Any CVV security number

## Live Project URL
The project has been deployed to Heroku and can be seen by opening [books-bazaar-08785163d42b.herokuapp.com](https://books-bazaar-08785163d42b.herokuapp.com/) in a web browser.

## Screenshots
### Homepage Hero with navigation and products
<div align="center"><img src="readme-images/screenshots/homepage/homepage-hero.png" alt="Image of the homepage hero section with affordance of product listings"></div>

### Homepage Product Listings
#### Classics
<div align="center"><img src="readme-images/screenshots/homepage/homepage-classics.png" alt="Image of the homepage Classics product section"></div>

#### Fiction
<div align="center"><img src="readme-images/screenshots/homepage/homepage-fiction.png" alt="Image of the homepage Fiction product section"></div>

### Homepage Latest Reviews
<div align="center"><img src="readme-images/screenshots/homepage/homepage-reviews.png" alt="Image of the homepage Reviews section"></div>

## User Experience
### Epics
- [Website Structure](https://github.com/DanielleDaly/portfolio-project-5/issues/5)
- [Product Search](https://github.com/DanielleDaly/portfolio-project-5/issues/6)
- [Shopping Process](https://github.com/DanielleDaly/portfolio-project-5/issues/11)
- [User Account](https://github.com/DanielleDaly/portfolio-project-5/issues/18)
- [Website Owner Admin](https://github.com/DanielleDaly/portfolio-project-5/issues/21)

### User Stories
- Website Structure
    - [Homepage Website Intro](https://github.com/DanielleDaly/portfolio-project-5/issues/1)
    As a website user I can see an introduction to the website so that I can know more about what the website sells
    - [Website Navigation](https://github.com/DanielleDaly/portfolio-project-5/issues/2)
    As a website user I can navigate through the website so that I can see the different products and pages within the website
    - [Contact Page](https://github.com/DanielleDaly/portfolio-project-5/issues/4)
    As a website user I can see a "Contact Us" page so that I can contact the company
    - [Interaction Notifications](https://github.com/DanielleDaly/portfolio-project-5/issues/17)
    As a website user I can see notifications of my interactions with the website so that I know what changes I have made or if I have placed an order, etc.
    - [Site Footer](https://github.com/DanielleDaly/portfolio-project-5/issues/35)
    As a website user I can see links to the most important parts of the site in the footer so that I can navigate through the site quickly
    - [Custom 404 Page](https://github.com/DanielleDaly/portfolio-project-5/issues/36)
    As a user I can see an error page when I go to a broken link so that I know that I should navigate back to a working page
    - [Company Information Page](https://github.com/DanielleDaly/portfolio-project-5/issues/3) NOT DONE - The website is self explanatory so there is no need for an About page. This is not a page always found on an e-commerce website

- Product Search
    - [All Products Listing](https://github.com/DanielleDaly/portfolio-project-5/issues/7)
    As a customer I can see a listing of all products so that I can view all of the website's products in one place
    - [Products by Category](https://github.com/DanielleDaly/portfolio-project-5/issues/8)
    As a customer I can search by category so that I can see products for only a specific category
    - [Search by Product Name](https://github.com/DanielleDaly/portfolio-project-5/issues/9)
    As a customer I can search by a product name (book title / stationary product name) so that I can find a specific product easily
    - [Sort Products by Price](https://github.com/DanielleDaly/portfolio-project-5/issues/10)
    As a customer I can list the products sorted by price so that I can see products listed in ascending or descending order by price

- Shopping Process
    - [Product Details](https://github.com/DanielleDaly/portfolio-project-5/issues/12)
    As a customer I can see the product details, description and image so that I know about the product before buying it
    - [Add Product to Shopping Cart](https://github.com/DanielleDaly/portfolio-project-5/issues/13)
    As a customer I can add a product to my shopping cart so that I can see it in the checkout
    - [Edit Shopping Cart](https://github.com/DanielleDaly/portfolio-project-5/issues/14)
    As a customer I can edit the contents of my shopping cart so that I can finalise the products that I want to purchase
    - [Checkout](https://github.com/DanielleDaly/portfolio-project-5/issues/15)
    As a customer I can checkout with the contents of my shopping cart so that I can receive my products
    - [Order Confirmation](https://github.com/DanielleDaly/portfolio-project-5/issues/16)
    As a customer I can receive confirmation of my order so that I know my order has been placed and what the contents of the order are
    - [Shopping Cart Total in Navigation](https://github.com/DanielleDaly/portfolio-project-5/issues/30)
    As a customer I can see my current shopping cart total so that I know the total cost of the items in my shopping cart
    - [Select the Size and Quantity of a Product](https://github.com/DanielleDaly/portfolio-project-5/issues/33)
    As a customer I can select the size and quantity of a product when making a purchase so that I can get the product variation that I want
    - [Enter My Payment Information Securely](https://github.com/DanielleDaly/portfolio-project-5/issues/34)
    As a customer I can enter my payment information securely during checkout so that I can feel that my payment card details are secure

- User Account
    - [User Details](https://github.com/DanielleDaly/portfolio-project-5/issues/19)
    As a customer I can save my details to an account so that I can see my details and details of orders I have placed
    - [Order Details](https://github.com/DanielleDaly/portfolio-project-5/issues/20)
    As a customer I can see my previous order details so that I know what I have purchased from the website in the past
    - [Register for a User Account](https://github.com/DanielleDaly/portfolio-project-5/issues/31)
    As a website user I can register for a User Account so that enter my details and view my orders
    - [Login and Logout](https://github.com/DanielleDaly/portfolio-project-5/issues/32)
    As a website user I can login and logout of my User Account so that I have secure access to my account

- Website Owner Admin
    - [Add / Edit Products](https://github.com/DanielleDaly/portfolio-project-5/issues/22)
    As a website owner / admin I can add and edit products easily so that I can manage what is available to purchase on the website
    - [Delete Products](https://github.com/DanielleDaly/portfolio-project-5/issues/23)
    As a website owner / admin I can delete products so that I can prevent customers from purchasing products that are no longer available
    - [Admin Area](https://github.com/DanielleDaly/portfolio-project-5/issues/24)
    As a website owner / admin I can access an admin area so that I can review products, orders, users and perform other administrative tasks

## Wireframes
- For the initial phase of design for the project I created wireframe layouts using [Balsamiq](https://balsamiq.com/). You can download these wireframes in PDF format but using the appropriate links below:
    - Desktop
        - Wireframe layouts for Desktop
    - Tablet
        - Wireframe layouts for Tablet
    - Phone
        - Wireframe layouts for Phone

## Database Models and Schema
### Models
- Users
    - User
        - From the Django Allauth package containing the username, email, and password
    - Userprofile
        - Model containing the user's details which can be re-used when placing future orders

- Products
    - Product
        - Contains the product information for each product item that is available in the store
    - Category
        - Contains the category information for products in the store

- Reviews
    - Contains the information for the Product Reviews

- Customer Enquiries
    - CustomerEnquiry
        - Contains the information for the Customer Enquiries submitted on the Contact Us page

- Checkout (Orders)
    - Order
        - Contains the information for an order, including the customer and the order contents
    - OrderLineItem
        - Contains the information on the individual line items in an order including the product and quantity

- Database Diagram
    - Below you will see the Database Diagram which shows the structure of the models in the database and the relationships between objects
    