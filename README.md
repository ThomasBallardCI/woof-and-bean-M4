# [View The Live Project Here](https://woof-and-bean-ci-m4-3f6e86d7432d.herokuapp.com/)

## Woof and Bean

Woof and Bean is a coffee and dog lovers' e-commerce website. Users can purchase various coffee-related paraphernalia and the perfect toy or treat for their special canine friend all in one place. By browsing via specific categories and using sorting filters such as name, date added, and category, as well as searching for keywords, the user can quickly find exactly what they are looking for. The basic functionality of the site comprises the user being able to register for a private account, log in and out, create orders by paying via Stripe, and receive confirmation emails when the order is created. Additional functionality has been added to the user experience, and these details will be discussed further in this document.

!["Am I Responsive" image](docs/images/amiresponsive.jpg)

## User Experience (UX)
### Project Goals

The goal of Woof and Bean is to provide a functional e-commerce experience to simulate the ability for users to browse products, add them to the cart, check out, receive order confirmation emails, and have a record of past orders within their account.

* When developing Woof and Bean, the main goal was to improve upon the basic functionality as outlined above in this document and enhance the user experience further. The additional functionality is as follows:
Users can easily create and edit a private wishlist while still being able to add the products directly to their shopping cart from the wishlist itself.
    * A contact form for the user to be able to contact the site admins with queries, issues, or suggestions, and then receive an email confirmation that their message was successfully sent.
* Accessibility was at the forefront of design and development. Using a contrasting colour palette ensures the site is easily accessible to users regardless of abilities, making the experience more enjoyable for all.

### User Stories
#### Viewing and Navigation
* View the website on a range of device sizes and have it be aesthetically pleasing and functional.
* View a range of coffee and dog products for sale.
* View individual product details.
* Easily view the total of my purchases at any time.
* View what products (if any) are on my wishlist
* View past order details on my profile
#### Registration and User Accounts
* Easily register for an account
* Easily log in or log out
* Easily recover my password in case I forget it
* Receive an email confirmation after registering
* Have a personalised user profile
* Be able to easily contact the site owners and receive confirmation of my message
#### Sorting and Setting
* Sort the list of available Products
* Sort by specific category of Product
* Search for a product by title or specific words in product details
* Easily see what I've searched for and the number of results found
* Be shown on a product details page whether a particular product is on my wishlist or not
#### Purchasing and Checkout
* Easily select the quantity of a product when purchasing it
* View items in my bag to be purchased
* Adjust the number of individual items in my bag
* Easily enter my payment information
* Feel my personal and payment information is safe and secure
* View an order confirmation after checkout
* Receive an email confirmation after checking out
#### Admin and Store Management
* Add products
* Edit/update products
* Delete products

## Design
### Colour Scheme

![Image of colour scheme](docs/images/woofandbeancolorpalette.jpg)

The colour scheme of Woof and Bean is primarily comprised of Onyx, White, and Peach.

* The background is Onyx to ensure the site is not bright and harsh on the eyes of the user when browsing products.
* The site text is predominately White and Peach, to ensure readability but also to provide enough contrast with the Onyx background matching the brand logo colours.
* The Choice of colours chosen along with eye strain and readability in mind matches that of the company logo invoking a premium or luxury feeling.

### Typography

[Google Fonts](https://fonts.google.com/) Was used to import the font featured on the site. The Font used is of the type sans-serif for consistency.

![Image of Stripe Element Font](docs/images/poppins-font.jpg)
* I adjusted the Stripe element font to use "Poppins" to bring it in line and consistent with the rest of the website typography.

![Image of Body Font and Title Font](docs/images/poppins-font.jpg)
* I chose the "Poppins" font for both the header and body of the site to keep a consistent and legible font throughout. Utilising Uppercase and bold font weights to highlight headers and important information for the user to pay attention to.

### Icons and Images

* All icons used throughout the site were provided by [FontAwesome](https://fontawesome.com/) as their style is aesthetically pleasing while being consistent and easily understandable.
* I sourced an icon from [Flaticon](https://www.flaticon.com) that will be attributed in the credits section of this document. I then used [Favicon](https://favicon.io/) to convert this .png to an icon file and imported that to my site. I installed a Favicon to help users distinguish this tab from others in their browser, the simple coffee bean design achieves this.
* All product images will be attributed in the credits section, along with the hero image on the home page.
* The home page image serves to provide an aesthetically pleasing and luxurious feel to the page while making clear that this site is a premium seller of boutique coffee and dog paraphernalia.

### Models
I created 2 unique models for this project, Contact, and Wishlist, and designed a model schema diagram to illustrate the relationship between models. I used [DrawSQL](https://drawsql.app/diagrams) to create these diagrams and was limited by the data types available on their site so some of the data types listed are incorrect. The accurate data and model field types can be found in each respective models.py file but I still wanted to use this software to illustrate the relationship between models. The DrawSQL site doesn't allow Foreign Keys to be attached to the entire model and so I have had to link fields to other specific fields where again this is inaccurate to the actual models. Below is the model diagram purely for representational purposes.
![Model image](/docs/images/models.jpg)

### Features
Woof and Bean is comprised of 11 core sections: Home page, Signup, Login, Profile, Wishlist, Products view, Product Details, Shopping Bag view, Checkout, Checkout Success and Contact Us.

* All pages feature the main nav bar, on desktop this includes the title, and search bar which can search for terms in Product titles, Categories, and Descriptions. The My Account drop-down features Product Management which is only accessible to the superuser (or site management) and can be used to add, edit, or delete products. The My Wishlist page and My Profile pages can also be accessed through this dropdown, along with being able to log out if a user is logged in. The Contact form is accessible through the Contact Us Navigation link on the main Navbar, and the bag icon displays up-to-date bag information which can be clicked to bring the user to the Shopping Bag page. The main navbar also features a Home page link for users on mobile and the All Products link drop-down shows all products, products by category, and products by price that can be filtered in the menu. Canine allows users to select and view only products relating to dogs with a drop-down menu to allow the user to choose either all Canine, treats, and toys specifically, similarly, the Coffee link on the nav bar allows the user to choose all coffee-related products, Accessories and beans/pre-ground.
* Each page also includes a footer displaying copyright information and social media links for the site.
* All pages on the site are responsive across multiple different screen sizes, on smaller screens like mobile phones the top navbar is condensed into a hamburger menu to ensure the screen isn't cluttered while maintaining the same functionality as that found on larger screens.
* For all actions a user performs on the site a pop-up message will appear either confirming that their requested action has been successful or giving them details of the action they've just performed. For example, adding, removing, or altering a product in the shopping bag will all be accompanied by messages unique to the action performed.

| Section | Feature | Photograph or gif |
| --- | --- | --- |
| The Home page features an image of a woman and her dog in a luxurious coffee shop, along with a call to action alerting the user new collections have arrived in store with a large bright "shop now" button to encourage the user to view all the products | Upon loading the site users are greeted with the home page image which aims to convey the luxurious nature of the site draw their attention to the large shop now button as the colours pop against the background image of a woman in a coffee shope with her dog and this immediately conveys the purpose of the site as one that products for dog and coffee lovers | ![Home Image](/docs/images/home-image.jpg) |
| The Sign Up page allows users to register for an account with the site | The sign up form encourages users who already have an account to sign in instead by showing both a text link and button to redirect users to the Log In page | ![Sign Up Form](/docs/images/sign-up.jpg)
| | The Sign Up form asks users to input their email address which must be unique to their account, and choose a username which again must be unique to their account and has a maximum length set by Django as 150 characters. The username field permits users to use special characters, numbers and letters to allow for usernames to be unique if there's a large client base. The form then asks the user to set a password, confirm their password and click the Sign Up button. All fields on the Sign Up form are required and the user cannot click Sign Up without successfully filling in these fields. | |
| The Log In page allows users to log who have registered for an account to log in to their already existing account | It encourages users who do not yet have an account to register before attempting to log in by providing a text link to the Sign Up page | ![Sign In page](/docs/images/sign-in.jpg) | 
| | The Log In form asks users to input their username, or email and their password, if a username or password combination is entered that doesn't exist an error displays stating "The username and/or password you specified are not correct" | ![Log In error](/docs/images/username-password-error.jpg) |
| | There is a radio button with the text 'Remember me' that allows users to select whether they want their log in information to be saved for the next time they visit the site | ![Remember me box](/docs/images/remember-me.jpg) | 
| | Django comes with ready-made password reset functionality so users are able to click a link stating they forgot their password. This redirects them to a page where they can enter their email address and an email with a link to reset their password is sent to their specified email address | ![Password Reset](/docs/images/password-reset.jpg) |
| The Profile page includes sections for a user's default delivery information, and their order history | The Profile page allows users to input their default delivery information so this information can be saved to their account and autofill on the checkout page, this isn't only a quality of life change but might encourage more users to go through with a purchase if the system is quick and easy | ![Default Delivery Information](/docs/images/default-delivery.jpg) | 
| | The Profile page displays a user's order history with information including their order number, date and time of purchase, the items and quantities ordered, and their order total. When the order number is clicked it brings users to their order confirmation which is initially displayed after a purchase made been made | ![Order History](/docs/images/order-history.jpg) |
| The Wishlist page allows users to view, remove, and add to basket products in their wishlist, though only if they are logged in | If a user has no items on their wishlist they are met with a message. 'Your wishlist is empty to add products visit a product page and click "add to wishlist"' | ![No products in wishlist view](/docs/images/wishlist-empty.jpg)|
| | When a user has added an item to their wishlist they can view this product in their Wishlist page, here the product image, name, price, date added, and two actions an add to bag button that add's the product to the users bag and a remove button that removes the product from the users wishlist. | ![Wishlist with products](/docs/images/wishlist.jpg) |
| The Products view shows all products available for sale, it allows users to browse all available products, filter them by category, and to sort by price, rating, alphabetised name, and alphabetised category. | Clicking any of the category buttons takes the user to a page that only displays products that match their request. The 'sort by...' box allows users to sort from low to high on price and rating. | ![All Products view](/docs/images/all-products.jpg) |
| | The product pages (whether All products or a filtered category page) displays the products in cards with the product image, title, price, and the category tag. For site managers like the superuser, there are also edit and delete buttons for product stock control. Due to the amount of products displayed on each page there is a back-to-top button to allow users to quickly and easily return to the top of the page | ![All Products Cards](/docs/images/all-products-card.jpg) |
| The Products Detail page is accessed when a user clicks on the title or image of a product on the All Products (or any product category) page. Each product detail page shows information about that product exclusively, along with letting users add it to their wishlist, choose a quantity, and add it to their bag. | This page displays the Products image, title, price, category tags, and description. If a user adds a product to their bag a message pops up confirming that this item has been added, and the bag icon in the navbar updates based on the price. | ![Product details page](/docs/images/product-details.jpg) |
| | The 'add to wishlist' button is featured above the product details below the category tag and when clicked adds the product to the user's Wishlist page. If a product is in a user's wishlist this button changes its text to say 'Already in wishlist' to let users know the product is already in their wishlist | ![remove from wishlist](/docs/images/already-in-wishlist.jpg) |
| The Shopping Bag view is accessed by clicking the bag icon in the navbar, this page shows the current contents of the bag along with product information | If nothing is in the bag text stating 'Your bag is empty' will display along with a button encouraging users to keep shopping. When an item (or multiple) is added a success message is displayed in the top right corner of the screen to let users know that their product has been added to the bag. This message explains which product, the quantity added along with the price, and a message that has calculated how much more the user would need to spend to get free delivery. | ![Add to bag success message](/docs/images/add-to-bag-success.jpg) |
| | After clicking the bag icon the user sees the contents of their bag, including the product image, name, sku, price, quantity and subtotal. The quantity of the product selected can be altered here using the quantity input, if this is altered the subtotal adjusts accordingly, items can also be removed from the bag using the remove button. The bag total is displayed lower down the page along with the delivery cost and grand total, with another message stating how much more the user would need to spend to receive free delivery. From here the user can either click 'keep shopping' to return to the products page, or click 'secure checkout' to proceed to the checkout page | ![Shopping bag page](/docs/images/shopping-bag.jpg) |
| The checkout page shows an order summary and then asks the user to fill out the details, delivery, and payment form to complete their order | The order summary consists of the product image, name, and quantity with its subtotal. The Delivery cost and grand total are displayed again | ![Checkout Summary](/docs/images/checkout-summary.jpg) |
| | The checkout form is comprised of fields for Full Name, Email Address, Phone Number, Street Address, Town or City, Post Code, and a dropdown country selector. There is also a radio button where users can opt to save this delivery information to their profile if they're logged in. If a user has previously opted to save information to their profile this form will be auto-populated. The payment field is at the bottom of the form where users can enter their card details, along with a button that either redirect the user back to their bag or complete their order with Stripe validating their details. There is also a message displayed in red underneath this 'Complete Order' button to warn users that their card is about to be charged, and how much. All required fields of the form must be entered for the 'Complete Order' button to be clicked and the order to be successfully processed. When the 'Complete Order' button is clicked a peach overlay appears on screen with a spinning arrow circle to demonstrate that the order is being processed. | ![Checkout Form](/docs/images/checkout.jpg) |
| The checkout success, or thank you page is reached after an order has been processed and displays the order information | The page confirms that the order has gone through successfully and tells the user which email their confirmation will be sent to. An example of this confirmation email is shown in the images section of this table, and upon deployment this will send the confirmation email to the user's real email address | ![Order confirmation email](/docs/images/order-confirmation-email.jpg) |
| | The order success page confirms the following details: order number, order date, the item(s) ordered along with the quantity, the full delivery details provided, and the full billing information. Below this is a button encouraging users to 'Continue Shopping' which would redirect them to the all products page| ![Order confirmation](/docs/images/order-confirmation.jpg) |
| The Contact form can be accessed whether a user is logged in or not, and simply asks users to fill in the following information: their name, email, subject line, and message, a button is shown below to allow users to submit their message | All fields in this form are required and the form cannot be submitted without all being filled in correctly | ![Contact Form](/docs/images/contact-form.jpg) |
| | The contact form is set up to send a confirmation email to the user with their message subject, and content repeated back to them so they have a copy of the communication. The email also states that Woof and Bean will respond within 48 hours, but if the message is urgent a contact number is listed | ![Contact form confirmation](/docs/images/contact-confirmation.jpg) |

* Future Implementations:
  * Ideally, I would like to implement a stock count feature for site managers and admin to be notified by email when the stock of an item is getting low.
  * I'd like to implement a stock available feature to show the user the remaining stock on an item.
  * In the future, I'd like to implement functionality that would allow the user to go to a product details page by clicking on the name or image of the product in their bag, due to time constraints I couldn't get this working in time for submission.
  * I also would like to add a rating functionality to the products and give the users the ability to rate products they have previously purchased so the product rating can be shown to new and existing customers.

### Accessibility

* Throughout the development of this site accessibility was a priority, semantic HTML, alt tags, and aria-labels are used wherever possible to assist screen readers. The font chosen is I believe, legible regardless of the screen size the user is on.

* Lighthouse gave my site a score in the 90's this demonstrates that I have prioritised accessibility throughout development and have implemented accessible features where needed whilst not compromising on the company brand and colour scheme.
    
    ![Lighthouse Accessibility Score](/docs/images/accessibility.jpg)

### Wireframes
During development I utilised the boutique ado walkthrough layout as a template and adjusted the styling to fit my needs. The two custom models (Contact and Wishlist) I wireframed out in a style to fit the rest of the site seamlessly.

* [Contact Desktop](/docs/images/contact-desktop.jpg)
* [Contact Mobile](/docs/images/contact-mobile.jpg)
* [Wishlist Desktop](/docs/images/wishlist-desktop.jpg)
* [Wishlist Mobile](/docs/image/wishlist-mobile.jpg)

### Languages Used
Woof and Bean used HTML, CSS, Python, and Javascrip

### Frameworks, Libraries, and Programs Used
* [Adobe XD](https://helpx.adobe.com/uk/support/xd.HTML) was used to create the Wireframes seen above.
* [AWS](https://aws.amazon.com/) to hold media files.
* [Bootstrap](https://getbootstrap.com/) was utilised to create a core HTML structure similar to Boutique Ado so that my time could be spent on providing functionality.
* [CI Python Linter](https://pep8ci.herokuapp.com/#)
* [Coolors](https://coolors.co/) to create a colour palette for this README document.
* [Django](https://www.djangoproject.com/) was used as a Python framework.
* [ElephantSQL](https://www.elephantsql.com/) was used to host the database for this site.
* [Favicon](https://favicon.io/) was utilised to create a Favicon for the site's browser tab.
* [Font Awesome version 6](https://fontawesome.com/) was used for all icons seen across the site.
* [GitHub](https://github.com/) was used to store the repository for this project.
* [Gitpod](https://www.gitpod.io/) is the environment in which this project was created and worked on.
* [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools) Was used as a debugging tool, and to help visualise the site in different screen sizes to ensure that user experience remained clean and efficient no matter the screen size.
* [Google Fonts](https://fonts.google.com/) provided the links for the font used on the site and aided in selecting a font that is complimentary to the Woof and Bean brand.
* [Heroku](https://www.heroku.com/?) was used in addition to GitHub as the deployment platform for this site due to the use of databases.
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) was used as a templating language.
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) to test the quality and responsiveness of each page on the site.
* [AmIResponsive!](https://ui.dev/amiresponsive) Aided in the creation of a multi-device mockup image so that I could test the appearance of the site on multiple device sizes, and provided the image seen at the beginning of this document.
* [W3C Markup Validator](https://validator.w3.org/) to validate HTML
* [Jigsaw W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate CSS used

### Deployment
Woof and Bean is deployed using Heroku by the following steps:

Elephant SQL:
-
    1. Go to [ElephantSQL](https://www.elephantsql.com/) and either create an account or log in via GitHub
    2. Click the 'Create New Instance' button
    3. Choose your plan (The Tiny Turtle free plan is acceptable), name your instance and leave the tags blank if you wish, then click the 'Select Region' button
    4. Select a data centre that is closest to you
    5. Click the 'Review' button
    6. Double check your details then click the 'Create Instance' button
    7. Navigate to the ElephantSQL dashboard and click on the database instance name you provided for this project
    8. In the URL section copy the database URL to your clipboard
    9. We will shortly return to this tab so leave it open

Heroku:
-
    1. Log into Heroku and click the 'New' button, then the 'Create a new app' button
    2. Enter a name for your app (this must be unique), choose the region that is closest to you and click the 'Create app' button
    3. Click 'Reveal Config Vars'
    4. Navigate back to your ElephantSQL tab and ensure the database URL is copied to your clipboard
    5. On Heroku add a config var named 'DATABASE_URL' and paste your ElephantSQL database URL as the accompanying value, then click 'Add'
    6. Add all other necessary environment variables to this config var section from your project's .env file apart from the DEVELOPMENT variable
    7. Find the 'Deploy' tab for your app on Heroku and click it
    8. In the Deployment method section click 'Connect to GitHub', type your repo name and click 'Connect'
    9. Click 'Enable Automatic Deploys' to ensure that your GitHub repository and Heroku are synced if you make any further code or project changes
    10. Click 'Deploy Branch' to let Heroku begin building the site
    11. We must now initialise our empty database by clicking 'More' then 'Run console'
    12. In the terminal that has appeared type 'from woof-and-bean import db' and click enter
    13. Now type 'db.create_all()' and hit enter again
    14. Type 'exit()' to exit the Python terminal and close the console, our Heroku database will now contain the tables and columns created from our models.py files
    15. Click the 'Open app' button to visit your built site


AWS (Amazon Web Services):
-
    1. Navigate to [AWS](https://aws.amazon.com/), log in or create an account if you don't already have one
    2. Search for S3 in Services, and click the 'Create bucket' button
    3. Enter a bucket name (this should relate to your Heroku app name), and select the region closest to you
    4. Uncheck 'Block all public access' and acknowledge that the bucket will be public, click 'ACLs enabled' and 'Bucket owner preferred', click 'Create bucket'
    5. Click the bucket instance you just created and navigate to the Properties tab
    5. Scroll down to 'static website hosting' and click 'use this bucket to host a website'
    6. Enter default values of index.HTML for the Index document, and error.HTML for the Error document then click 'Save'
    7. On the Permissions tab paste the following code into the CORS configuration editor: 
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
    8. Click 'Save'
    9. Navigate to 'Bucket Policy' and select 'policy generator', the type of which is 'S3 Bucket Policy', type * into the Principal field, and select 'get object' for the action
    10. Copy your ARN from the Bucket Policy tab and paste this into the ARN field on the policy generator page, then click 'Add Statement', then 'Generate Policy'
    11. Copy the code displayed to your clipboard and paste this into the Bucket Policy editor. Before saving add a '/*' to the end of the Resource key, then click 'Save'
    12. Navigate to the 'Access Control List' tab, click 'edit' and enable List for Everyone (public access) and accept the warning box
    13. From the AWS site search for 'IAM', click 'User Groups' and then click 'Create New Group'
    14. Name this group something that makes sense for the logic of your project, I named this 'manage-woof-and-bean', then click 'Create Group'
    15. From the IAM dashboard click 'Policies' then 'Create Policy'
    16. Click the 'JSON' tab and select 'import policy', search for 'S3' and import the 'AmazonS3FullAccess' policy
    17. Find your arn from the Bucket Policy page in S3 and copy it, paste this into the 'Resource' key in the JSON tab instead of the '*' value. The format should be
    "Resource": [
        'your_arn_here',
        'your_arn_here/*'
    ]
    18. Click 'Review Policy', and give it a name and description, e.g name: woof-and-bean-policy, description: Access to S3 bucket for woof and bean static files
    19. Click 'Create Policy'
    20. Navigate back to the 'User Groups' page and click on the group you created
    21. Click 'Attach Policy', search for the policy you just created and select it, then click 'Attach Policy'
    22. Finally navigate to the 'Users' page and click 'Add User'
    23. Create a user named 'your-site-name-staticfiles-user', my username was 'woof-and-bean-staticfiles-user', click 'Next' then select the group we created earlier and click 'Next' again and 'Create User' to add your user to this group
    24. In the Identity and Access Management tab click on Users, and click on the username of the user you just created
    25. Click the 'security credentials' tab, scroll down to 'access keys' and click 'create access key'
    26. On the 'Access key best practices & alternatives' page click 'Other' as our use case, follow this process to the end and click the 'download .csv' button
    27. Save this .csv file as they are only available to us once and will be used to authenticate our user from our Django app

Back in the Gitpod CLI:
-
    1. Type 'pip3 install boto3' into the terminal
    2. Type 'pip3 install django-storages' into the terminal
    3. Type 'pip3 freeze > requirements.txt' into the terminal to update this file
    4. In settings.py add 'storages', to our installed apps
    5. Still in settings.py add the following code:
    if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'your_aws_bucket_name_here'
    AWS_S3_REGION_NAME = 'your_aws_region_name_here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    6. Navigate to Heroku and add these AWS keys to our config variables, the AWS_ACCESS_KEY_ID, and AWS_SECRET_ACCESS_KEY can be found in the .csv file we downloaded and saved earlier
    7. Add the key 'USE_AWS' with the value 'True' (without quotation marks) to our Heroku config vars
    8. Back in our workspace create a base-level file called 'custom_storages.py' and add the following code:
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage

    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION
    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    9. Add, commit and push your changes using the syntax 'git add .', 'git commit -m "add a message here", 'git push'

Back on AWS:
-
    1. Navigating to our bucket we can now see a static folder in our bucket containing all of our static files
    2. In S3 click 'Create folder' and name this folder 'media', click 'Save'
    3. Click the just created 'media' folder, then click 'upload', 'Add files' and select all the product and site images for the website
    4. Click 'Next' and under 'manage public permissions' select 'grant public read access to this object(s)', click 'Next' again and click 'Upload'

In Django admin:
-
    1. Login to your superuser account on the Django admin
    2. Click 'email addresses' and set your superuser's email address to verified and primary

Stripe:
-
    1. Login to your Stripe account, click 'Developers' and 'API keys' and locate your publishable key and secret key
    2. Check these keys and values are added to your Heroku config vars, if not add them now
    3. Create a new webhook endpoint by going to Webhooks in the Developers menu, click 'Add endpoint' and paste your deployed url here but add '/checkout/wh/' to the end of the url, click to receive all events then click 'Add endpoint'
    4. Click to reveal your Signing secret and add this value to your Heroku config vars
    5. Ensure all the variables in Heroku config vars match the names you've provided in your settings.py file

Your deployed site should now appear and function the same way as your development site with all static and media files loading and displaying appropriately


How to Fork Woof and Bean:
-
    1. Login to your GitHub account
    2. Navigate to the 'woof-and-bean-m4' repository and click the 'Fork' button in the top right corner

How to Clone Woof and Bean:
-
    1. Login to your GitHub account
    2. Navigate to the 'woof-and-bean-m4' repository
    3. Click the green 'Code' button next to the 'Gitpod' button
    4. Click 'Open with GitHub desktop'
    5. Click the 'Choose...' button and navigate to a local path where you wish to store the cloned repository
    6. Click the 'Clone' button

## Testing
### Automated Testing

### W3 Nu HTML Validator
The W3 Nu HTML Validator was used multiple times throughout development to ensure the HTML used was all up to industry standards, the results are as follows:

* [Home page](/docs/images/home-html.jpg)
* [Sign Up page](/docs/images/signup-html.jpg)
* [Log In page](/docs/images/login-html.jpg)
* [Product Management page](/docs/images/product-management-html.jpg)
* [Wishlist page](/docs/images/wishlist-html.jpg)
* [Profile page](/docs/images/profile-html.jpg)
* [Contact Us page](/docs/images/contact-html.jpg)
* [All Products page](/docs/images/all-products-html.jpg)
* [Product Detail page](/docs/images/product-detail-html.jpg)
* [Shopping Bag page](/docs/images/shopping-bag-html.jpg)
* [Checkout page](/docs/images/checkout-html.jpg)
* [Checkout Success page](/docs/images/checkout-success-html.jpg)

### W3C CSS Validation Service
The W3C CSS Validation Service was used to validate the two CSS files contained within the project, the results are as follows:

* [Base.css](/docs/images/base-css-validation.jpg)
* [Profile.css](/docs/images/profile-css-validation.jpg)

### JS Hint
JS Hint was used to validate the JavaScript found throughout the project with the results being:

* [Profile](/docs/images/profile-js-hint.jpg)
* [Stripe](/docs/images/stripe-js-hint.jpg)
* [Quantity Input Calculator](/docs/images/quantity-input-script-js-hint.jpg)

### Python Linter

The following files were tested with a [Python Linter](https://pep8ci.herokuapp.com/) to ensure PEP8 compliance, and all files apart from settings.py passed with no errors.

* [Bag contexts.py](/docs/images/bag-contexts.jpg)
* [Bag urls.py](/docs/images/bag-urls.jpg)
* [Bag views.py](/docs/images/bag-views.jpg)
* [Checkout admin.py](/docs/images/checkout-admin.jpg)
* [Checkout forms.py](/docs/images/checkout-forms.jpg)
* [Checkout models.py](/docs/images/checkout-models.jpg)
* [Checkout signals.py](/docs/images/checkout-signals.jpg)
* [Checkout urls.py](/docs/images/checkout-urls.jpg)
* [Checkout views.py](/docs/images/checkout-views.jpg)
* [Webhook-handler.py](/docs/images/webhook-handler.jpg)
* [Webhooks.py](/docs/images/webhooks.jpg)
* [Contact admin.py](/docs/images/contact-admin.jpg)
* [Contact forms.py](/docs/images/contact-forms.jpg)
* [Contact models.py](/docs/images/contact-models.jpg)
* [Contact urls.py](/docs/images/contact-urls.jpg)
* [Contact views.py](/docs/images/contact-views.jpg)
* [Home urls.py](/docs/images/home-urls.jpg)
* [Home views.py](/docs/images/home-views.jpg)
* [Products admin.py](/docs/images/products-admin.jpg)
* [Products forms.py](/docs/images/products-forms.jpg)
* [Products models.py](/docs/images/products-models.jpg)
* [Products urls.py](/docs/images/products-urls.jpg)
* [Products views.py](/docs/images/products-views.jpg)
* [Products widgets.py](/docs/images/products-widgets.jpg)
* [Profile forms.py](/docs/images/profiles-forms.jpg)
* [Profile models.py](/docs/images/profiles-models.jpg)
* [Profile urls.py](/docs/images/profiles-urls.jpg)
* [Profile views.py](/docs/images/profiles-views.jpg)
* [Woof and Bean settings.py](/docs/images/settings.jpg) - settings.py in the Woof and Bean app was the only file to show line length warnings, these affected the AUTH_PASSWORD_VALIDATORS and were not created, or updated by myself so I have left them as Django intended.
* [Woof and Bean urls.py](/docs/images/woofandbean-urls.jpg)

### Flake8
After using the CI Python linter to individually check the compliance of each Python page I used the command 'python3 -m flake8' in the terminal to further check for anything I may have missed. The results of this are below:
![Flake8 1](/docs/images/flake8-1.jpg)
![Flake8 2](/docs/images/flake8-2.jpg)

The only unresolved errors I got back were as follows:
* Errors related to .vscode files these lines were not ones that I created or edited in any way.
* The same as above goes for errors concerning the migrations files which comprised the majority of these linting warnings.
* The checkout webhooks file is flagged for the variable 'e' being assigned but not used however this variable has been assigned to catch exceptions or errors in the code that may occur with webhooks and Stripe.
* The contact views.py file warns that three variables 'name', 'subject', and 'content' are assigned but never used, these variables need to be assigned so that they can be accessed in the confirmation email sent to users
* Setting.py file is showing line length issues again these lines are generated by Django as explained above as well as flagging unused imports that as far as I'm aware are being used.
* No other errors or warnings were documented and I feel confident that the project is up to industry standard for Python conventions.




bug - NoReverseMatch at /profile/whishlist/ when trying to include html for mobile wishlist view
        fix = putting mobile includes inside forloop for wishlist items

bug - after refactoring shopping basket code for mobile devices increment and decrement buttons would allow users to decrement and increment bellow 1 and above 99
    Fix = Change Id's to classes for quantity form and adjusted JS to look for class elements.

bug - Server error 500 when signing up for account - fix = create runtime.txt with older version of python for heroku to use

bug - stripe webhooks failing. - Fix added missin / to the end of the webhook name

Bug - logo image not loading after heroku deployment - fix: Adjusted image src link for AWS hosting
src="https://woof-and-bean-ci-m4.s3.amazonaws.com/media/wblogo.png"

Search bar icon inside input on the right helped by Slack London community