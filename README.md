# Home Plate

Home Plate is a restaurant management app built with Django, PostgreSQL, and Materialize CSS. Using the app, front of house staff can create covers, input orders, generate tickets, and close orders. Admin accounts can also edit the menu and staff accounts.

### Models: 
* Covers
* Tickets
* Menu Items

### Functions:
* Full CRUD on Covers, Tickets, Menu Items, Staff
* Bill and tip calculation
* Point of Sale
* Print tickets (PDF)
* Staff authentication

### Views: 
* Home/Control Panel
    * Shielded behind login
    * Button + Nav Access to Menu Manage, Staff Manage, Create Cover, View Covers
* Login Panel
* Menu Management Panel (full CRUD in view)
* Staff Managment Panel (full CRUD in view/use Admin panel?)
* Create Cover
* View Covers
    * Click to access View/Modify Cover
* View/Modify Cover > full Ticket CRUD in view + Print Tickets
* Close Cover > Point of Sale

## Roadmap:
### Completed:
* Initialization, create superuser, create database
* Model: Covers
* Model: Tickets
* Model: Menu Items
* Routes, Views, Placeholder Templates
* Import Materalize + shop for functionality
* View Homepage
* View: View Tables
* View: Create Table
* View: Table Detail (RUD on Table plus CRUD on Tickets)
* Function: Print Tickets
* Function: Calculate Bill/Tips/Tax

* View: Close Cover
* Function: Point of Sale
* Function: Staff authentication
* CSS: Home Page/Login
* CSS: Menu Management
* CSS: View Tables (Use Collapsible!)
* CSS: Create Table
* CSS: Table Detail
* CSS: Close Table

### Materialize Functionality to Use
* Color Palette, Grid, Helpers (valign), Shadows
* Buttons, Cards, Icons
* Auto Init, Collapsible Dropdown, MODALS (USE FOR FORMS??), Tooltips, Waves
* FORMS FORMS FORMS
### Stretch Goals
* Print Menu
* Ticket Splitting
* Entrees come with sides
* Set time zone in admin
* Dietary info for menu items
* Description for menu items
* Descriptions for orders (well done, no cheese etc)
* State by State sales tax

### Django Collector Requirements:
Full CRUD on one model
One-To-Many or Many-To many relationship between 2 models
Custom CSS or a CSS library/framework

