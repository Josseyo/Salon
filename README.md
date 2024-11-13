# SalonTalks

SalonTalks is a fully functioning e-commerce web application that allows users to view and purchase tickets to SalonTalks events online. Users can easily create personal accounts and profiles to access their information and order history. The site also enables administrators to manage events and respond to contact inquiries. The live site can be found [here](https://salon-talks-af192748bd52.herokuapp.com).

## Table of Contents
- [The SalonTalks](#salontalks)
- [UX](#ux)
- [Typography](#typography)
- [Color Palette](#color-palette)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Site Pages](#site-pages)
  - [User Features](#user-features)
  - [Admin Features](#admin-features)
- [Future Features](#future-features)
- [Tools & Technologies Used](#tools--technologies-used)
- [Database Design](#database-design)
- [Agile Development Process](#agile-development-process)
  - [GitHub Projects](#github-projects)
  - [GitHub Issues](#github-issues)
  - [MoSCoW Prioritization](#moscow-prioritization)
- [Ecommerce Business Model](#ecommerce-business-model)
- [Search Engine Optimization (SEO) & Social Media Marketing](#search-engine-optimization-seo--social-media-marketing)
  - [Keywords](#keywords)
  - [Sitemap](#sitemap)
  - [Robots](#robots)
- [Testing & Validation](#testing--validation)
- [Deployment](#deployment)
  - [Postgres SQL Database](#postgres-sql-database)
  - [Amazon AWS](#amazon-aws)
    - [S3 Bucket](#s3-bucket)
    - [IAM](#iam)
    - [Final AWS Setup](#final-aws-setup)
  - [Stripe API](#stripe-api)
  - [Gmail API](#gmail-api)
  - [Heroku Deployment](#heroku-deployment)
  - [Local Deployment](#local-deployment)
    - [Cloning](#cloning)
    - [Forking](#forking)
- [Credits](#credits)
- [Content](#content)
- [Media](#media)
- [Acknowledgements](#acknowledgements)

## UX
The design philosophy focuses on creating a clear and engaging experience for the target customers. Relevant information is presented in a salient and clean manner, allowing users to navigate easily through the site to browse and make purchases.

## Typography
For a website targeting an older audience, readability and clarity are prioritized:

- **Headings:** Lato Bold
- **Body Text:** Open Sans Regular
- **Button Text/CTA:** Lato

All fonts are available for free on [Google Fonts](https://fonts.google.com/selection?query=open+sa).

## Color Palette
The color palette was created using [Coolors](https://coolors.co/db6c1b-704c5e-fdf9f8-000000-7d8570-ffffff) and evaluated with ChatGPT:

![Color Palette](documentation/design/colors.png)

### Readability & Accessibility
The palette combines warm tones with calming colors, ensuring good contrast for readability. Here are the key colors used:

- **Cocoa Brown (#DB6C1B):** Versatile for buttons and text on light backgrounds.
- **Eggplant (#704C5E):** Adds depth and sophistication, suitable for secondary text.
- **Snow (#FDF9F8):** Soft white for backgrounds, enhancing brightness.
- **Black (#000000):** Primary text color providing depth.
- **Reseda Green (#7D8570):** Calming background color.

## User Stories
All user stories can be found in the linked GitHub project [here](https://github.com/users/Josseyo/projects/8).

![Kanban Board](documentation/project_setup/kanban_userstories.png)

## Wireframes
Explore the [Balsamiq wireframes](https://balsamiq.cloud/sr8qece/ptjxrgq).

### Homepage
![Home](documentation/wireframes/Home.png)
- **Header:** Logo, Navigation (Home, Products, About, Contact), Search
- **Main:** Cover image with call to action and ticket purchase button
- **Footer:** Social media links

### Event List View
![Event List View](documentation/wireframes/Event_list.png)
- **Header:** Same as homepage
- **Main:** Sort options, Grid of products
- **Footer:** Social media links

### Product Detail Page
![Event Details View](documentation/wireframes/Event_detail.png)
- **Header:** Same as homepage
- **Main:** Event details with images, description, and purchase options
- **Footer:** Social media links

### Shopping Bag
![Shopping Bag](documentation/wireframes/Bag.png)
- **Header:** Same as homepage
- **Main:** List of cart items with total cost and checkout options
- **Footer:** Social media links

### Checkout
![Checkout](documentation/wireframes/Checkout.png)
- **Header:** Same as homepage
- **Main:** Shipping and payment information
- **Footer:** Social media links

### Checkout Success
![Checkout Success](documentation/wireframes/Checkout_success.png)
- **Header:** Same as homepage
- **Main:** Order confirmation details
- **Footer:** Social media links

### Email Order Confirmation
![Confirmation Email](documentation/wireframes/Email_confirmation.png)
- **Content:** Order summary and customer information

### My Account
![My Account](documentation/wireframes/My_account.png)
- **Header:** Same as homepage
- **Sections:** Profile, Order History, Payment Methods
- **Footer:** Social media links

### Mobile Views
![Mobile Example Views](documentation/wireframes/Mobile_views.png)

## Features

### Existing Features
- Discount feature
- Meeting link included in order confirmation
- The links for all purchased products are included in the confirmation email.
- The links are not visible in the product details or shop until after purchase.
- Manage products and contact requests from frontend
- Newsletter subscription signup

### Site Pages

| Home Page | Mobile View |
|-----------|-------------|
| ![Home Page](documentation/features/sitepages/home.png) | ![Home Page Mobile](documentation/features/sitepages/home_mobile.png) |

<div style="width: 100%; max-width: 600px; margin: 0 auto;">
    The main homepage for the site. The hero image is large and striking. A large heading tells users they are in the right place, and a call to action button invites users to enter and explore the site products.
</div>


#### Footer
![Footer with Social Links](documentation/features/sitepages/social_links.png)

### Event List View
| Event List View | Sort Options |
|------------------|--------------|
| ![Event List View](documentation/features/sitepages/all_product_list.png) | ![Sort Options](documentation/features/sitepages/sort_options.png) |

<div style="width: 100%; max-width: 600px; margin: 0 auto;">
    Displays the Salons available for the user to purchase. Displays images of products and their essential information including title, description, price, category, start time and end time. Salons are displayed in a pleasing responsive grid layout, making it easy for a user to browse the Salons. Salons utilise a mouse-hover animation to add to the interactivity of the page. Salons can also be filtered and sorted by event/name, date, time, category, host. 
	Administrators viewing this page can see links under each Salon to edit or delete the event.
</div>

### Categories
![Categories](documentation/features/sitepages/categories_product_lists_page.png)
Events are categorized for easy navigation.

### Event Detailed View
| Event Detailed View | Success Bag Toast |
|---------------------|-------------------|
| ![Event Detail View](documentation/features/sitepages/product_detail.png) | ![Success Bag Toast](documentation/features/sitepages/success_bag_toast.png) |
<div style="width: 100%; max-width: 600px; margin: 0 auto;">


### Shopping Bag
![Shopping Bag](documentation/features/sitepages/checkout.png)

Displays all items currently in the user's shopping basket. Users get a message if their basket is empty, otherwise they will see a list of events that they have selected with a button to navigate to the events page, and another to navigate to the checkout page.

### Checkout Page
![Secure Checkout](documentation/features/sitepages/secure_checkout.png)

Displays an order summary of the items that are being prepared for purchase with accompanying item details. Displays a total cost of the order to the user. The user also sees a form to fill in their personal details. For logged in users, these details will be pre-filled if the user has provided that information in the past. A checkbox allows users to save entered information to their profile. A payment input form exists at the bottom of the page for a user to enter their payment card information. A message below this warns the user that advancing will complete the purchase and incur a charge to their card.

### Checkout Success Page
![Order Success](documentation/features/sitepages/order_success.png)

Displays a thank you message to the user, as well as a message telling the order confirmation has been emailed. An order summary with all the relevant information, including a unique order number and the purchased event link is displayed.

### Email Order Confirmation
![Email Order Confirmation](documentation/features/sitepages/email_order_confirmation.png)

The order confirmation email includes the same information as the checkout success page. It also include information how to contact us for any queries.

### About Page
![About Page](documentation/features/sitepages/about.png)
<div style="width: 100%; max-width: 600px; margin: 0 auto;">
 Gives users essential information about The SalonTalks. At the end of the text a "Browse SalonTalks" button is visible to keep the user engaged with the presented information.


### FAQ
![FAQ](documentation/features/sitepages/faq.png)

FAQ Page. Displays the most frequently asked questions about the site. Lets users know essential information and quells worries that they may have about the site and its products. Animation and accordion serve to make the information engaging and clean.

### Contact
![Contact Page](documentation/features/sitepages/contact.png)

 Users can contact the site owner using the contact form. Users can choose from a selection of subjects and leave their message via the text box.

### Contact Success
![Contact Success Page](documentation/features/sitepages/message_sent.png)

Users see this page after sending a contact message via the contact page. This page serves to confirm to the user that their message has been sent successfully. A short message informs the user that their contact message has been received, and that one of the team will respond as soon as possible

### Newsletter Subscription
![Newsletter Subscription](documentation/features/sitepages/newsletter_subscription.png)

Users can signup for Newsletter subscription. The subscription form can be found in the navbar on all pages. 

![Newsletter subscription](documentation/features/sitepages/subscription_signup_suv.png)

Users see a confirmation toast after subscribing.

![Newsletter subscription](documentation/features/sitepages/already_subscribed_toast.png)<br>

The user will be notified if the email has already been subscribed.<br><br>


In the newsletter there will be an unsubscribe link in case the user change their mind.

### Custom Error Pages
![404 Page](documentation/features/sitepages/404.png)

These provide a more user-friendly error page than the user would see otherwise and includes an informative message and button to return to the home of the site.

## User Features

### User Registration
![Signup](documentation/features/sitepages/signup.png)
Users can register for an account using a front-end form. This creates a user object in the database and automatically secures the user's sensitive information

![signup verification email](documentation/features/sitepages/signup_verification_email.png)

When user has signed up they receive an email verification.


### User Login
![User Login](documentation/features/sitepages/signin.png)
Users who have made an account can quickly and easily log in to their account in order to access the login-required functionality of the site.
#### Login Redirect
![login verification message](documentation/features/sitepages/login_message.png)
After logging in, the user are sent to the home page. A message shows that you are logged in and shows if you have something placed in your shopping bag.

#### Login Dependant Navbar Links<br>
![dependant navbar links](documentation/features/sitepages/dependant_nav.png)
<br>
When users are logged in 'Register' and 'Login' links are replaced with 'My Account' links. This provides the user with visual feedback upon logging in, as well as removing links that they will not need


### User Logout
![User Logout](documentation/features/sitepages/signout.png)
Users who are logged in can easily log out in order to stop access to their account-based information and functionality

### User Password Recovery
![Password Recovery](documentation/features/sitepages/pwd_reset.png)
Users who have forgotten their password can recover their password via the forgot password link on the login page. Users will enter their email and get a password reset link sent to their account email which they can use to set a new password.

### User Profile
![User Profile](documentation/features/sitepages/my_profile_with_orders.png)
User profiles are automatically created upon user registration. Displays a user's profile information. Lets a user see their relevant profile information in a clean and simple way, and contains an update form that users can use to update their profile information. Users can also see their order history, with full details of their order as well as links to see past order confirmations.

## Admin Features

### Add and Edit Product Page
![Edit/Delete Links](documentation/features/sitepages/edit_delete_links.png)

If you are logged in as administrator you will see links under each event to edit (blue link) or delete (red link) the event.
![edit event](documentation/features/sitepages/edit_event.png)
**Add Event** Administrators can use a front-end form to create new site products. The form is simple and clean and automatically formats and displays the created product in the same manner as existing products. The form is found under My Account/Product management

**Edit Event** Administrators can use a front-end form to update existing events. If the current logged-in user has admin (superuser) privileges, an edit button will appear under products which allows that user to edit the product's details.

### Contact Response
![Contact Requests/Response list](documentation/features/sitepages/contact_response_list.png)

Admins can see a list of all of the contact messages sent by users. Messages are displayed in an easy-to-read table, with all of the salient information presented. Messages are automatically sorted with those messages which have not been responded to at the top of the list, with the oldest (the message which has gone unanswered the longest) at the top. Admins can click on the view details links to see the full contact messages, as well as respond to the message.

### Contact Details Page
![Contact Response details page](documentation/features/sitepages/contact_response.png)
Admins can see details of a contact message left by the user. All of the contact message's information can be seen, including email, name, subject, message, and whether this contact message has been responded to. Contact messages can be responded to or deleted via the large buttons at the bottom of the page. A link navigates back to the contact requests page

**Response Alert**
![Response alert](documentation/features/sitepages/response_alert.png)

Once a response is sent, the contact message is automatically marked as "Responded," and the "respond to message" button will no longer be visible on that message's details page.

### Webhooks
The site uses a secure and robust webhook system to ensure that the payment process are not interrupted and corrupted, either through user error or malicious intent. Webhooks are incorporated via the Stripe payment system and are handled on the Stripe website, by way of the python code in checkout > webhook_handler.py and checkout > webhooks.py
## Future Features

- **Remaining Seats**: Limit ticket availability.
- **Real-Time Updates**: Use JavaScript for dynamic updates of total cost and ticket quantities, automatically remove past events, and update remaining tickets in real-time.
- **Subscription Model**: Implement a subscription payment option for access to all SalonTalks, utilizing Django groups and Stripe integration for backend management and webhook updates.
- **Newsletter Customization**: Develop a system for admins to customize and send newsletters, including a front-end form for text and images, integrated into newsletter views.
- **Complete remaining user stories**: See the project backlog.


## Tools & Technologies
List of tools and technologies utilized in the project.

- **HTML**: Main site content.
- **CSS**: Site design and layout.
- **JavaScript**: User interactions.
- **Python**: Back-end programming.
- **Git**: Version control (git add, commit, push).
- **GitHub**: Secure online code storage.
- **Gitpod**: Cloud-based IDE for development.
- **Bootstrap**: Front-end CSS framework for responsiveness and components.
- **Django**: Python framework for the site.
- **PostgreSQL**: Relational database management.
- **CI Database**: PostgreSQL database service.
- **Psycopg2**: PostgreSQL database adapter.
- **Heroku**: Hosting for the back-end.
- **Stripe**: Secure online payments.
- **AWS S3**: Static file storage.
- **Allauth**: User authentication system.
- **Pillow**: Image processing library.
- **Gunicorn**: WSGI server.
- **Crispy Forms**: Auto-formatting for front-end forms.
- **asgiref**: ASGI utilities for Django.
- **boto3**: AWS SDK for Python.
- **botocore**: Core functionality for AWS SDK.
- **dj-database-url**: Database URL parsing for Django.
- **django-allauth**: User authentication system.
- **django-appconf**: Application configuration for Django.
- **django-countries**: Country field for Django forms.
- **django-crispy-forms**: Enhanced form handling in Django.
- **django-extensions**: Extensions for Django development.
- **django-storages**: Storage backends for Django.
- **django-tinymce**: WYSIWYG editor for Django.
- **jmespath**: JSON query language.
- **oauthlib**: OAuth library for Python.
- **PyJWT**: JSON Web Token implementation.
- **python3-openid**: OpenID support for Python.
- **pytz**: Time zone support for Python.
- **rcssmin**: CSS minification library.
- **requests-oauthlib**: OAuth for requests library.
- **rjsmin**: JavaScript minification library.
- **s3transfer**: S3 transfer manager for boto3.
- **sqlparse**: SQL parsing library.
- **stripe**: Stripe API for payments.
- **django-csp**: Content Security Policy middleware for Django.

https://temp-mail.org/

## Database Design
![ERD](documentation/project_setup/erd.svg)

The relationships between the models in the ERD:

1. **Order and OrderLineItem**:
   - **Relationship**: One-to-Many
   - **Description**: An `Order` can contain multiple `OrderLineItems`. Each `OrderLineItem` is associated with a single `Order`, indicating that it represents a specific product within that order.

2. **OrderLineItem and Product**:
   - **Relationship**: Many-to-One
   - **Description**: Each `OrderLineItem` is linked to one `Product`. A `Product` can appear in multiple `OrderLineItems`, reflecting that the same product can be ordered multiple times in different orders.

3. **Order and UserProfile**:
   - **Relationship**: Many-to-One
   - **Description**: An `Order` is associated with one `UserProfile`. Each `UserProfile` can have multiple `Orders`, representing the order history for that user.

4. **Product and Category**:
   - **Relationship**: Many-to-One
   - **Description**: Each `Product` belongs to one `Category`. A `Category` can contain multiple `Products`, allowing for organization of products into different categories.

5. **UserProfile and Order**:
   - **Relationship**: One-to-Many
   - **Description**: A `UserProfile` can have multiple `Orders`, tracking the order history for that user profile.

6. **SubscribeRequest and Subscribe**:
   - **Relationship**: Many-to-One
   - **Description**: Each `SubscribeRequest` is linked to one `Subscribe`. This indicates that a subscription request is made for a specific subscription type.

7. **CollaborateRequest and Contact**:
   - **Relationship**: Many-to-One
   - **Description**: Each `CollaborateRequest` can be associated with one `Contact`. This shows that a collaboration request may be part of a broader contact inquiry.

---
## Agile Development Process

### GitHub Projects
[GitHub Projects](https://github.com/users/Josseyo/projects/8/views/1) served as an Agile tool for this project. Through it, user stories, labels, epics and milestone tasks were planned, then tracked using the basic Kanban board.
Epics were decomposed into smaller User Stories and Tasks. The Github issue linking system was utilised to ensure that user stories which were children of an epic were kept organised and easily accessible through these links
- [Userstories]
- [Epics](https://github.com/users/Josseyo/projects/8/views/2?sliceBy%5BcolumnId%5D=Status&sliceBy%5Bvalue%5D=EPIC)
- [Milestones]

Overview of issues tracked in the GitHub repository.
- [Open issues](https://github.com/users/Josseyo/projects/8/views/1)
- [Closed issues](https://github.com/users/Josseyo/projects/8/views/2?sliceBy%5BcolumnId%5D=Status&sliceBy%5Bvalue%5D=Done)

### MoSCoW Prioritization
The MoSCoW method was used with accompanying custom Github project labels to help prioritise the important tasks for the available time.
- **Must Have:** Core functionalities for MVP.
- **Should Have:** Important features for future development.
- **Could Have:** Enhancements for user experience.
- **Will Not Have:** Features for future consideration.

## Ecommerce Business Model
SalonTalks operates on a Business-to-Customer (B2C) model, focusing on one-time transactions.
Currently in the early stages of development, the site features a newsletter signup form and links for social media marketing. Utilizing social media can help create a community around the business and increase site traffic, particularly on larger platforms like Facebook.

The newsletter list enables the business to communicate regularly with users, providing updates on last-chance events, new offerings, host announcements, and more.

## Search Engine Optimization (SEO) & Social Media Marketing

### Keywords

**Keywords**  
I’ve identified several relevant keywords to enhance the site’s visibility in search engines. This includes a mix of:

- **Short-tail (head terms)**: General keywords.
- **Long-tail keywords**: More specific phrases.

I also experimented with [Word Tracker](https://www.wordtracker.com) to analyze the frequency of some primary keywords for my site, but only until the free trial ended.

### Sitemap & Robots
To help search engines find and index the site more effectively I added a sitemap in the root directory as well as a robots.txt with default settings instructions for web crawlers.

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) and the [deployed site URL:](https://salon-talks-af192748bd52.herokuapp.com) 
to generate the sitemap.xml file.

- [sitemap.xml](sitemap.xml)
- [robots.txt](robots.txt) `

Links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)


### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales. Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've used the
[Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip)
provided by Code Institute, to create a mockup Facebook business account using

![facebook](documentation/webmarketing/facebook.png)

### Newsletter Marketing

A sign-up form is availble on the site to allow users to submit their
email address to subcsribe to our newsletter.


## Testing & Validation

Features and workflows were manually tested across different screen sizes and browser compatibility. The code was validated with:

- **HTML**: Validated using the [W3C HTML Validator](https://validator.w3.org/)
- **CSS**: Validated using the [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
- **JavaScript**: Validated using [JS Hint](https://jshint.com)
- **Python**: Validated using the [CI Python Linter](https://pep8ci.herokuapp.com/)
- **Performance**: Validated using [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
- **Accessibility**: Validated using the [Wave Validator](https://wave.webaim.org/) 

**See detailed [Test Report](documentation/TESTING.md)**
**See [Bug Report](documentation/BUGS.md)**



## Deployment
The live site is deployed on heroku and can be found here [deployed site URL:](https://salon-talks-af192748bd52.herokuapp.com) 

### Postgress SQL Database
Details about the SQL database setup.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).


#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Suggested Name: `group-salontalks` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Suggested Name: `policy-salontalks` (policy + the project name)
	- Provide a description:
		- "Access to S3 Bucket for SalonTalks static files."
	- Click **Create Policy**.
- From **User Groups**, click your "group-salontalks".
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-salontalks") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Suggested Name: `user-salontalks` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-salontalks`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://salon-talks-af192748bd52.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)


### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or salontalk
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user's own value")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/josseyo/salon) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/josseyo/salon.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/josseyo/salon)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/josseyo/salon)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!



Here’s an improved version of the "Credits" section for your README file, with better organization and clarity:

---

## Credits


### Contributors

### Resources and Tutorials
- **Django eCommerce Tutorial**: Comprehensive guide for building an eCommerce site using Django.
  - [GitHub Repository](https://github.com/imanaspaul/Django-eCommerce-tutorial-manascode/blob/master/ecommerce/ecommerce/settings.py)
  - [Part Two - Django Allauth](https://manascode.com/django-e-commerce-tutorial-part-two-django-allauth/)
  
- **Web Piano Academy**: Reference for readme and contact management.
  - [GitHub Repository](https://github.com/LewisMDillon/web-piano-academy/blob/main/README.md)

- **EmailJS**: Service for sending emails from your application.
  - [EmailJS Website](https://www.emailjs.com/)

- **Django Stripe Tutorial**: Guide for integrating Stripe payment processing.
  - [Learn Django](https://learndjango.com/tutorials/django-stripe-tutorial#configure-stripe)

- **Code Institute Course**: Resource for understanding Django fundamentals.
  - [Course Material](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+4/courseware/eb05f06e62c64ac89823cc956fcd8191/9c06563251a34ed19f5d4273ab4d55ab/?child=first)

- **FAQ Creation**: 
  - [Django Easy FAQ](https://pypi.org/project/django-easy-faq/)

- **Newsletter Subscription**:
  - [Building an Email Newsletter Subscriber in Django](https://dev.to/shubhamkshatriya25/how-to-build-a-email-newsletter-subscriber-in-django-j2p)
  - [Django Forum Discussion on Subscription Options](https://forum.djangoproject.com/t/how-to-add-subscribe-option-in-a-django-website/12449)

- **Data Corruption Solutions**:
  - [Stack Overflow Discussion](https://stackoverflow.com/questions/38970832/session-data-corrupted-in-django)

- **Custom Error 404 Page**:
  - [YouTube Tutorial](https://www.youtube.com/watch?v=Tsmjxh4bj8k)

- **SEO Best Practices**:
  - [Google Developers - Robots Meta Tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
  - [Keyword Validation Tool](https://www.wordtracker.com/search?query=book%20discussions)


### Content
ChatGPT has been used to create categories, product descriptions, product images and evaluate the color palette.

### Media
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements
Code Institute for providing lms, tutorsupport 
Rory Sheridan my mentor for valuable tips and support
Christina Åhman for laughter and support 
Lotta Tuvstedt for the idea and help with content

### Issues on the road
October 4th I got pull & push issues when trying to update previous pushed commits accordin to followin instructions https://algerwrites.medium.com/how-to-remove-env-from-git-commit-history-1d594917b376 . On tutors recommendation I started a new workspace. Which resulted in confusion with code and commits being "broken". 73 pulled and 78 pushed but got stuck in the middle. 

