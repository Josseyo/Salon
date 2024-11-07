

## Table of Contents
- [The Salon](#the-salon)
- [UX](#ux)
- [Typography](#typography)
- [User Stories](#user-stories)
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
- [Social Media Marketing](#social-media-marketing)
- [Newsletter Marketing](#newsletter-marketing)
- [Testing](#testing)
- [Deployment](#deployment)
- [ElephantSQL Database](#elephantsql-database)
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


## The SalonTalks
SalonTalks is a fully functioning e-commerce web application. The site allows users to view and purchase tickets to SalonTalks events online. Users can easily create personal accounts and profiles and see their information and order history on the site. The site also enables administrators to add, edit and remove events as well as view and respond to contact enquiries.

## UX
The design philosophy was to create a clear and engaging look for the target customers. Relevant information is presented in a salient and clean manner, allowing the user to easily navigate through the site to browse and make their purchase as well as finding contact information for more help and support.

### Typography

When choosing fonts for a website with an older audience, especially those who may have vision problems, it's important to prioritize readability and clarity. 

**Headings:** Lato bold
**Body text:** Open Sans regular
**Headings:** Button text/CTA: Lato 

All these fonts are available for free on 
[Google Fonts](https://fonts.google.com/selection?query=open+sa)


### Color Palette
I have used [coolors](https://coolors.co/db6c1b-704c5e-fdf9f8-000000-7d8570-ffffff) to create the color palette for the project. Then I have evaluated the palette using ChatGPT.

![here](https://github.com/users/Josseyo/projects/8)

![colors](documentation/design/colors.png)

**Cocoa Brown (#DB6C1B)**

This rich, warm brown maintains cohesion with the Rufous and Xanthous tones while providing good contrast. It’s a versatile color that could be used for buttons, text on light backgrounds, or accents.

**Eggplant (#704C5E)**

This subtle purple adds depth and sophistication to the palette. It contrasts nicely with the warmer tones (Cocoa Brown) without overwhelming them. Eggplant would work well for secondary text, borders, or backgrounds.

**Snow (#FDF9F8)**

This soft, almost ethereal white has subtle hints of warmth. It evokes a sense of tranquility and purity, enhancing the overall brightness of the design. Snow can be effectively used for backgrounds, providing a clean canvas that allows other colors to stand out, or for text on darker backgrounds to ensure readability.

**Black (#000000)**

The black adds depth to the palette. Utilized for primary text. Its versatility allows it to anchor the design, providing a strong foundation that balances the warmth of Cocoa Brown and the softness of Snow.

**Reseda Green (#7D8570)**

This muted green adds a nice balance to the palette. It’s calming and pairs well with brighter tones like the Cocoa Brown. It can be great for backgrounds or secondary elements, as it doesn't dominate the visual space.

### Readability & Accessibility:
The color palette feels well-balanced, combining warm tones with a touch of calmness from the Eggplant and Reseda Green. The earthy and muted tones will give your website a grounded, inviting feel without being too loud. 

The palette has good contrast when pairing lighter colors with the darker colors. This ensures that text and buttons remain readable for all users

### User Stories
All user stories can be found in a linked GitHub project [here](https://github.com/users/Josseyo/projects/8)

![kanban](documentation/project_setup/kanban_userstories.png)


## Features
Overview of features included in the project.

### Existing Features
Description of features that are currently available.

### Site Pages
The main homepage for the site. Hero image is large and striking with a call to action button to invite users to enter and explore and purchase events.
![home page](documentation/features/sitepages/home.png)

![Event list view](documentation/features/sitepages/all_product_list.png)

![Event list view](documentation/features/sitepages/categories_product_lists_page.png)

![Cateory hover](documentation/features/sitepages/category_hover.png)

![Contact](documentation/features/sitepages/contact.png)

![faq](documentation/features/sitepages/faq.png)

![Event list view](documentation/features/sitepages/contact.png
)

### User Features
Features available to users.

### Admin Features
Features available to administrators.

## Future Features
Planned features for future updates.

**Integrate Real-Time Updates:**
   - Use JavaScript to dynamically update the total cost and any other relevant information as the quantity is adjusted so that the updates are smooth and do not require page refreshes.
   -  Automatically remove events when date of event has passed


## Tools & Technologies Used
List of tools and technologies utilized in the project.

https://temp-mail.org/

## Database Design
Overview of the database structure and design.

## Agile Development Process
Description of the agile process used for development.

### GitHub Projects
[GitHub Projects](https://github.com/users/Josseyo/projects/8/views/1) served as an Agile tool for this project. Through it, user stories, labels, epics and milestone were planned and tasks carried out, and tracked using the basic Kanban board.

The MoSCoW method was used with accompanying custom Github project labels to help prioritise the important tasks for the available time.

Epics were decomposed into smaller User Stories and Tasks

### GitHub Issues
Overview of issues tracked in the GitHub repository.

### MoSCoW Prioritization
Explanation of the MoSCoW prioritization method used.

## Ecommerce Business Model
Details about the business model for the ecommerce aspect.

## Search Engine Optimization (SEO) & Social Media Marketing
Strategies for SEO and social media marketing.

### Keywords
List of keywords relevant to the project.

### Sitemap
Overview of the website's structure.

### Robots
Instructions for web crawlers.

### Social Media Marketing
Details on social media marketing strategies.
![facebook](documentation/webmarketing/facebook.png)

### Newsletter Marketing
Information on newsletter marketing efforts.

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
Instructions for deploying the project.

### Postgress SQL Database
Details about the SQL database setup.

### Amazon AWS
Information on using Amazon AWS for the project.

### S3 Bucket
Details on the S3 bucket configuration.

### IAM
Information on Identity and Access Management.

### Final AWS Setup
Overview of the final setup on AWS.

### Stripe API
Details on integrating the Stripe API.

### Gmail API
Information on using the Gmail API.

### Heroku Deployment
Instructions for deploying on Heroku.

### Local Deployment
Steps for local deployment of the project.

### Cloning
Instructions for cloning the repository.

### Forking
Guidelines for forking the repository.

## Credits
Acknowledgment of contributors and resources.

FAQ setup - https://pypi.org/project/django-easy-faq/
Mail setup - 

SEO Keywords - https://www.wordtracker.com

### Content
Overview of the content used in the project.

### Media
Details about media assets utilized.

### Acknowledgements
Acknowledgments to individuals and organizations that contributed to the project.

### Issues on the road
October 4th I got pull & push issues when trying to update previous pushed commits accordin to followin instructions https://algerwrites.medium.com/how-to-remove-env-from-git-commit-history-1d594917b376 . On tutors recommendation I started a new workspace. Which resulted in confusion with code and commits being "broken". 73 pulled and 78 pushed but got stuck in the middle. 

