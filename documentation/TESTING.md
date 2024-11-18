# Manual Testing

<details>
<summary><strong>Fixes and improvements during validation</strong></summary>

## Features
- Wrapped the `<li>` elements under the parent `<ul>` tag where necessary to ensure proper HTML structure.
- Used `<style>` tag to remove the list bullets.
- Adjusted heading levels for better hierarchy.
- Added hidden visual links in forms for accessibility.
- Made the scroll-to-top link crawlable by adding a valid `href` attribute and included a `title` attribute for better accessibility and context.

## Accessibility Improvements
- Ensured that all links are crawlable by search engines.
- Added descriptive titles to enhance user experience.

## Rich Results Testing
![Rich text validation](validation/rich_text.png)

</details>

## Performance
**Validated using [Lighthouse](https://developers.google.com/web/tools/lighthouse/)**

### Home
![Home](validation/lighthouse/home.png)

### About
![About](validation/lighthouse/about.png)

### Bag
![Bag](validation/lighthouse/bag.png)

### Contact
![Contact](validation/lighthouse/contact.png)

### FAQ
![FAQ](validation/lighthouse/home.png)

### Event list view
![Products](validation/lighthouse/event_list.png)

### Event detail view
![Products](validation/lighthouse/event_details.png)

### Subscribe
![Subscribe](validation/lighthouse/subscription.png)

### Login
![Login](validation/lighthouse/login.png)

---

## HTML
**Validated using the [W3C HTML Validator](https://validator.w3.org/)**

### Home
![Home](validation/html/home_html.png)

### About
![About](validation/html/about_html.png)

### Bag
![Bag](validation/html/bag_html.png)

### Checkout
![Checkout](validation/html/checkout_html.png)

### Checkout Success
![Checkout Success](validation/html/checkout_success_html.png)

### Contact
![Contact](validation/html/contact_html.png)

### FAQ
![FAQ](validation/html/faq_html.png)

### Event list view
![Products](validation/html/events_list_html.png)

### Event detail view
![Products](validation/html/event_detail_html.png)

### Subscribe
![Subscribe](validation/html/newsletter_subscribe_html.png)

### Register Account
![Signup](validation/issues/remaining_issues/signup_html.png)

### Login
![Login](validation/html/login_html.png)

### Logout
![Logout](validation/html/logout_html.png)

### Forgot Password
![Forgot Password](validation/issues/remaining_issues/password_reset_html.png)

### Confirm email
![Forgot Password](validation/html/confirm_email_html.png)

### Create new password
![Create New Password](validation/html/new_pwd_html.png)

### My Account
![My Account](validation/html/my_account_html.png)

---

## CSS
**Validated using the [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)**

### Base
![Base](validation/css/base_css.png)
http://jigsaw.w3.org/css-validator/validator$link

### Checkout
![Checkout](validation/css/checkout_css.png)
http://jigsaw.w3.org/css-validator/validator$link

### FAQ
![Profile](validation/css/profiles_css.png)
http://jigsaw.w3.org/css-validator/validator$link

### FAQ
![Profile](validation/css/profiles_css.png)
http://jigsaw.w3.org/css-validator/validator$link

---

## JavaScript
**Validated using [JS Hint](https://jshint.com)**

### Stripe
![Stripe](validation/js/stripe_elements_js.png)

### Cookies
![Cookies](validation/js/cookies_js.png)

## Python
**Validated using the [CI Python Linter](https://pep8ci.herokuapp.com/)**

### About
![About](validation/python/about_py.png)

### Bag
![Bag](validation/python/bag_py.png)

### Checkout
![Checkout](validation/python/checkout_py.png)
![Checkout](validation/python/checkout_py2.png)
![Checkout](validation/python/checkout_py3.png)

### Common
![Common](validation/python/common_py.png)

### Contact
![Contact](validation/python/contact_py.png)
![Contact](validation/python/contact_py2.png)

### FAQ
![FAQ](validation/python/faq_py.png)

### Home
![Home](validation/python/home_py.png)

### Products
![Products](validation/python/products_py.png)
![Products](validation/python/products_py2.png)

### Salon
![Salon](validation/python/salon_py.png)

### Subscribe
![Subscribe](validation/python/subscribe_py.png)
![Subscribe](validation/python/subscribe_py2.png)
---

## Remaining issues

### Register Account
![Signup](validation/issues/remaining_issues/signup_html.png)

### Forgot Password
![Forgot Password](validation/issues/remaining_issues/password_reset_html.png)

---

## Fixed Bugs

### Email replies not working
![Email reply bug](bugs/email_reply_bug.png)
To fix this issue, I updated the Django version to 4.2. The error was occurring because Python 3.12 removed the keyfile and certfile parameters from the SMTP.starttls() method, but my current Django version (3.2.25) is still using these parameters.

### Bag being emptied
When I put items in the bag, they are being lost on the way to secure checkout.

![Email reply bug](bugs/empty_bag.png)

#### Problem

Heroku shows corrupted data:
2024-10-25T10:14:16.306229+00:00 app[web.1]: Session data corrupted
2024-10-25T10:14:16.306262+00:00 app[web.1]: Current bag state before adding: {}
2024-10-25T10:14:16.306263+00:00 app[web.1]: Adding quantity: 1 for item_id: 3
2024-10-25T10:14:16.306281+00:00 app[web.1]: Updated bag state: {'3': 1}
2024-10-25T10:14:16.392183+00:00 app[web.1]: 10.1.8.232 - - [25/Oct/2024:10:14:16 +0000] "POST /bag/add/3/ HTTP/1.1" 302 0 "https://salon-talks-af192748bd52.herokuapp.com/products/3/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
2024-10-25T10:14:16.392649+00:00 heroku[router]: at=info method=POST path="/bag/add/3/" host=salon-talks-af192748bd52.herokuapp.com request_id=9992286c-105c-441d-a098-5a42a3eac931 fwd="94.234.117.51" dyno=web.1 connect=0ms service=363ms status=302 bytes=423 protocol=https
2024-10-25T10:14:16.763505+00:00 app[web.1]: Session data corrupted
2024-10-25T10:14:16.763533+00:00 app[web.1]: Total: 0, Discount: 0, Grand Total: 0
2024-10-25T10:14:16.795029+00:00 app[web.1]: 10.1.8.232 - - [25/Oct/2024:10:14:16 +0000] "GET /products/3/ HTTP/1.1" 200 17926 "https://salon-talks-af192748bd52.herokuapp.com/products/3/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
2024-10-25T10:14:16.795479+00:00 heroku[router]: at=info method=GET path="/products/3/" host=salon-talks-af192748bd52.herokuapp.com request_id=6d7bc072-5405-402d-ab52-030405b9db9c fwd="94.234.117.51" dyno=web.1 connect=0ms service=266ms status=200 bytes=18349 protocol=https

#### Solution
To fix the issue I replaced the: SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", get_random_secret_key()) with: SECRET_KEY = os.environ.get('SECRET_KEY', '')

[Back to readme](../README.md)

