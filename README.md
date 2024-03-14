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
Woof and Bean is comprised of 11 core sections: Home page, Signup, Login, Profile, Wishlist, Products view, Product Details, Shopping Bag view, Checkout, Checkout Success, Contact Us.

* All pages feature the main nav bar, on desktop this includes the title, and search bar which can search for terms in Product titles, Categories and Descriptions. The My Account drop-down features Product Management which is only accessible to the superuser (or site management) and can be used to add, edit, or delete products. The My Wishlist page and My Profile pages can also be accessed through this dropdown, along with being able to log out if a user is logged in. The Contact form is accessible through the Contact Us Navigation link on the main Navbar, and the bag icon displays up-to-date bag information which can be clicked to bring the user to the Shopping Bag page. The main navbar also features a Home page link for users on mobile and the All Products link drop-down shows all products, products by category and products by price that can be filtered in the menu. Canine allows users to select and view only products relating to dogs with a drop-down menu to allow the user to choose either all canine, treats and toys specifically, similarly, the Coffee link on the nav bar allows the user to choose all coffee-related products, Accessories and beans/pre-ground.
* Each page also includes a footer displaying copyright information and social media links for the site.
* All pages on the site are responsive across multiple different screen sizes, on smaller screens like mobile phones the top navbar is condensed into a hamburger menu to ensure the screen isn't cluttered while maintaining the same functionality as that found on larger screens.
* For all actions a user performs on the site a pop-up message will appear either confirming that their requested action has been successful or giving them details of the action they've just performed. For example, adding, removing, or altering a product in the shopping bag will all be accompanied by messages unique to the action performed.

| Section | Feature | Photograph or gif |
| --- | --- | --- |
| The Home page features an image of a woman and her dog in a luxurious coffee shop, along with a call to action alerting the user new collections have arrived in store with a large bright "shop now" button to encourage the user to view all the products | Upon loading the site users are greeted with the home page image which aims to convey the luxurious nature of the site draw their attention to the large shop now button as the colours pop against the background image of a woman in a coffee shope with her dog and this immediately conveys the purpose of the site as one that products for dog and coffee lovers | ![Home Image](/docs/images/home-image.jpg) |
| The Sign Up page allows users to register for an account with the site | The sign up form encourages users who already have an account to sign in instead by showing both a text link and button to redirect users to the Log In page | ![Sign Up Form](/docs/images/sign-up.png)
| | The Sign Up form asks users to input their email address which must be unique to their account, and choose a username which again must be unique to their account and has a maximum length set by Django as 150 characters. The username field permits users to use special characters, numbers and letters to allow for usernames to be unique if there's a large client base. The form then asks the user to set a password, confirm their password and click the Sign Up button. All fields on the Sign Up form are required and the user cannot click Sign Up without successfully filling in these fields. | |
| The Log In page allows users to log who have registered for an account to log in to their already existing account | It encourages users who do not yet have an account to register before attempting to log in by providing a text link to the Sign Up page | ![Sign In page](/docs/images/sign-in.png) | 
| | The Log In form asks users to input their username, or email and their password, if a username or password combination is entered that doesn't exist an error displays stating "The username and/or password you specified are not correct" | ![Log In error](/docs/images/username-password-error.png) |
| | There is a radio button with the text 'Remember me' that allows users to select whether they want their log in information to be saved for the next time they visit the site | ![Remember me box](/docs/images/remember-me.png) | 
| | Django comes with ready-made password reset functionality so users are able to click a link stating they forgot their password. This redirects them to a page where they can enter their email address and an email with a link to reset their password is sent to their specified address | ![Password Reset](/docs/images/password-reset.png) |
| The Profile page includes sections for a user's default delivery information, and their order history | The Profile page allows users to input their default delivery information so this information can be saved to their account and autofill on the checkout page, this isn't only a quality of life change but might encourage more users to go through with a purchase if the system is quick and easy | ![Default Delivery Information](/docs/images/default-delivery.png) | 
| | The Profile page displays a user's order history with information including their order number, date and time of purchase, the items and quantities ordered, and their order total. When the order number is clicked it brings users to their order confirmation which is initially displayed after a purchase made been made | ![Order History](/docs/images/order-history.png) |
| The My Wishlist page allows users to view and edit their wishlist, though only if they are logged in | If a user has no items on their wishlist they are met with a message 'You currently have no books in your wishlist, click the button below to find your new favourite read...'. Along with a button that redirects users to the All Books page | ![No books in wishlist view](/docs/images/wishlist-empty.png) |
| | When a user has added an item to their wishlist they can view this book in their My Wishlist page, here the book cover image, title, author and blurb are displayed. The price on this page is displayed as the price for quality 'Great', with text explaining that qualities of 'Fair' and 'Good' will be reduced. There is also a button where users can remove this item from their wishlist. | ![Wishlist with book](/docs/images/wishlist.png) |
| The Products view shows all books available for sale, it allows users to filter by Genre or Special Offer and to sort by price, rating, alphabetised title, and alphabetised genre. | Clicking any of the genre/special offer buttons takes the user to a page that only displays books that match their request. The 'sort by...' box allows users to sort from low to high on price and rating, to let them find deals or the best books on the site | ![All Books view](/docs/images/all-books.png) |
| | The book pages (whether All Books or a filtered genre page) display books in cards with the book cover image, title, author, language, release year, price (for quality 'Great'), and the genre or special offer tag. If the book hasn't been rated or reviewed it stated 'No rating' but once reviews have been made it shows the average rating out of 5 aggregated across all users. For site managers like the superuser, there are also edit and delete buttons for product stock control. Due to the amount of books displayed on each page there is a back-to-top button to allow users to quickly and easily return to the top of the page | ![All Book Cards](/docs/images/all-books-card.png) |
| The Book Detail page is accessed when a user clicks on the title or image of a book on the All Books (or any genre/special offers) page. Each book detail page shows information about that book exclusively, along with letting users add it to their wishlist, add it to their bag, or rate or review the book | This page displays the book's image, title, author, average rating (if this has been rated, otherwise it shows 'This book hasn't been rated yet'), a button to bring users down to the rating and review form, book length, year of release, price, tags, and blurb. If a user adds a book to their bag a message pops up confirming that this item has been added, and the bag icon in the navbar updates based on the price. | ![Book details page](/docs/images/book-details.png) |
| | The 'add to wishlist' button is featured prominently above the cover image and when clicked adds the book to the user's My Wishlist page. If a book is in a user's wishlist this button changes its text to say 'Remove from wishlist' to let users manage their wishlist without having to go into their Wishlist page | ![remove from wishlist](/docs/images/remove-from-wishlist.png) |
| | The site uses dynamic pricing meaning that depending on the quality of the book a user selects and adds to their bag the price will be different. A 'Great' quality item is full price, 'Good' quality has a 20% discount applied, and a 'Fair' quality is discounted by 40% due to the second hand nature of the shop. This pricing is calculated dynamically but accurate item and grand totals are presented throughout the site. Underneath the quality the user can adjust the quantity of books they wish to add to their bag, this field cannot be manipulated to be lower than 1 or higher than 99. | ![Example of dynamic pricing](/docs/images/dynamic-pricing.gif) |
| The Book Reviews section is found on each book detail page and both displays all existing reviews from users and has a form in which users can submit their own rating and review | If no reviews have been made for a book there is text which states 'This book has no reviews yet...'. If reviews have been left they are displayed in a row which differs depending on screen size and utilises a horizontal scroll bar to display all reviews cleanly and clearly. Each review card shows the username of the reviewer, the review date (where more recent reviews appear first) and the stars they awarded the book out of 5. It is mandatory that stars be awarded to leave a review but submitting a written review is optional, if a written review is left it is displayed under the star rating. For the user who wrote each review that is displayed there will be edit and delete buttons only visible and accessible to them. If a user clicks the edit button they are taken to a form that is pre-populated with the content of their original review. If a user clicks the delete button a modal pops up asking if they are sure they wish to delete this as it's irreversible. In addition, only superusers can leave multiple reviews for each book (for development purposes) and users who attempt to leave multiple reviews for one book will be met with a message saying this cannot be done. | ![Book Review Section](/docs/images/book-reviews.png) |
| | The book review form itself is simple and lets users input a star rating and a written review (if they wish) before clicking the submit review button | There is a note telling users that they must add a star rating to submit the review, a star rating is left by hovering over the number star they wish to award the book. The written review field has a maximum character attribute of 3000 and if a written review becomes longer than the size of the review card a vertical scroll bar allows users to scroll through and read the full review without this cluttering the screen. | ![Book review form](/docs/images/book-review-form.png) |
| The Shopping Bag view is accessed by clicking the bag icon in the navbar, this page shows the current contents of the bag along with product information | If nothing is in the bag text stating 'Your bag is empty' will display along with a button encouraging users to keep shopping. When an item (or multiple) is added a success message is displayed in the top right corner of the screen to let users know that their book has been added to the bag. This message explains which book, in which quality and quantity has been added along with the price, and a message that has calculated how much more the user would need to spend to get free delivery. | ![Add to bag success message](/docs/images/add-to-bag-success.png) |
| | After clicking the bag icon the user sees the contents of their bag, including the book image, title, author, quality, and SKU. The quantity of the book selected can be altered here using the quantity input, if this is altered the subtotal adjusts accordingly, items can also be removed from the bag using the remove button. The bag total is displayed lower down the page along with the delivery cost and grand total, with another message stating how much more the user would need to spend to receive free delivery. From here the user can either click 'keep shopping' to return to the books page, or click 'secure checkout' to proceed to the checkout page | ![Shopping bag page](/docs/images/shopping-bag.png) |
| The checkout page shows an order summary and then asks the user to fill out the details, delivery, and payment form to complete their order | The order summary consists of the book cover image, title, author, quality, and quantity with its subtotal. The Delivery cost and grand total are displayed again | ![Checkout Summary](/docs/images/checkout-summary.png) |
| | The checkout form is comprised of fields for Full Name, Email Address, Phone Number, Street Address, Town or City, Post Code, and a dropdown country selector. There is also a radio button where users can opt to save this delivery information to their profile if they're logged in. If a user has previously opted to save information to their profile this form will be auto-populated. The payment field is at the bottom of the form where users can enter their card details, along with a button that either redirect the user back to their bag or complete their order with Stripe validating their details. There is also a message displayed in red underneath this 'Complete Order' button to warn users that their card is about to be charged, and how much. All required fields of the form must be entered for the 'Complete Order' button to be clicked and the order to be successfully processed. When the 'Complete Order' button is clicked a green overlay appears on screen with a spinning arrow circle to demonstrate that the order is being processed. | ![Checkout Form](/docs/images/checkout.png) |
| The checkout success, or thank you page is reached after an order has been processed and displays the order information | The page confirms that the order has gone through successfully and tells the user which email their confirmation will be sent to. A development example of this confirmation email is shown in the images section of this table, and upon deployment this will send the confirmation email to the user's real email address | ![Order confirmation email](/docs/images/order-confirmation-email.png) |
| | The order success page confirms the following details: order number, order date, the item(s) ordered along with the quantity, the full delivery details provided, and the full billing information. Below this is a button encouraging users to 'Check out the latest deals' which would redirect them to the clearance page and new releases page| ![Order confirmation](/docs/images/order-confirmation.png) |
| The Contact form can be accessed whether a user is logged in or not, and simply asks users to fill in the following information: their name, email, subject line, and message, a button is shown below to allow users to submit their message | All fields in this form are required and the form cannot be submitted without all being filled in correctly | ![Contact Form](/docs/images/contact-form.png) |
| | The contact form is set up to send a confirmation email to the user with their message subject, and content repeated back to them so they have a copy of the communication. The email also states the Second Hand Shelf will respond within 48 hours, but if the message is urgent a contact number is listed | ![Contact form confirmation](/docs/images/contact-confirmation.png) |

* Future Implementations:
  * Ideally, I would like to streamline the process for site managers to add products to the site, the form works fine with every detail being easily input apart from the book quality and price variable. Currently, for any new book added to the site, the manager must go into the store admin and create 3 quality attributes for the book, one for 'Great' quality with a price_factor of 1.0, one for 'Good' quality with a price_factor of 0.8, and one with 'Fair' quality with a price_factor of 0.6. This seems tedious, or at worst could be forgotten by management which may cause issues with the site
  * In the future I'd like to implement functionality whereby users could resell their own books through the site much like how a site manager would upload a product currently, however, this was beyond the scope of my project
  * I also wanted to potentially add a 'My Reviews' page to the site where users can view their own reviews of different books without having to search through all the existing reviews from other users. In addition, functionality whereby users could like or comment on others' reviews would make the site more engaging and interactive



bug - NoReverseMatch at /profile/whishlist/ when trying to include html for mobile wishlist view
        fix = putting mobile includes inside forloop for wishlist items

bug - after refactoring shopping basket code for mobile devices increment and decrement buttons would allow users to decrement and increment bellow 1 and above 99
    Fix = Change Id's to classes for quantity form and adjusted JS to look for class elements.

bug - Server error 500 when signing up for account - fix = create runtime.txt with older version of python for heroku to use

bug - stripe webhooks failing. - Fix added missin / to the end of the webhook name

Bug - logo image not loading after heroku deployment - fix: Adjusted image src link for AWS hosting
src="https://woof-and-bean-ci-m4.s3.amazonaws.com/media/wblogo.png"

Search bar icon inside input on the right helped by Slack London community

8 products per category

singals instances create and save

set up ready signals in apps.py import signals to activate

Add items to wishlist - using add item to bag views.py code as a base?

Add a contact model custom model 2





## User Stories

### As A/An Shopper
    - **Viewing and Navigation**

        | I Want To Be Able To...                                    | So That I Can...                                                                   | 
        |------------------------------------------------------------|------------------------------------------------------------------------------------| 
        | View a list of products                                    | Select some to purchase                                                            | 
        | View individual product details                            | Identify the price, description, product rating,<br> product image and available sizes |
        | Quickly identify deals,<br> clearance items and special offers | Take advantage of special savings on products<br> I'd like to purchase |
        | Easily view the total of my purchases at any time          | Avoid spending too much |

    - **Sorting and Searching**
        
        | I Want To Be Able To...                                    | So That I Can...                                                                   | 
        |------------------------------------------------------------|------------------------------------------------------------------------------------|
        | Sort the list of available products                        | Easily identify the best rated, best priced and<br> categorically sorted products |
        | Sort a specific category or products                       | Find the best-priced or best-rated product in a<br> specific category, or sort the products in that<br> category by name |
        | Sort multiple categories of products simultaneously        | Find the best-priced or best-rated products across<br> broad categories, such as "Treats" or "Accessories" |
        | Search for a product by name or description                | Find a specific product I'd like to purchase |
        | Easily see what I've searched for and the number of<br> results | Quickly decide whether the product I want is available |

    - **Purchasing and Checkout**
        
        | I Want To Be Able To...                                    | So That I Can...                                                                   | 
        |------------------------------------------------------------|------------------------------------------------------------------------------------|
        | Easily select the size and quantity of a product<br> when purchasing it | Ensure I dont accidentally select the wrong product,<br> quantity or size |


### As A/An Site User
    - **Registration and User Accounts**

        | I Want To Be Able To...                                    | So That I Can...                                                                   | 
        |------------------------------------------------------------|------------------------------------------------------------------------------------|
        | Easily register for an account | Have a personal account and be able to view my profile |
        | Easily login or logout | Access my personal account information |
        | Easily recover my password in case I forget it | Recover access to my account |
        | Receive an email confirmation after registering | Verfify that my account registration was successful |
        | Have a personalized user profile | View my personal order history, order confirmations<br> and save my personal information |


# Product Model
    "category" - Product category ForeignKey
    "sku" - product sku
    "name" - product name
    "description" - product description
    "price" - product price
    "rating" - product rating
    "image url" - product image url
    "image" - product image

# Profiles Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

# Category Model
    "name" - category name PrimaryKey
    "friendly_name" - friendly name for front end

# wishlist Model
    "User" - One to One field - User
    "products" - Many to Many field - Product
    "created" - date time field

# rating Model
    star choices 1,1 - 2,2 - 3,3 - 4,4 - 5,5
    "User" - foreignkey
    "product" - foreignkey
    "order" - foreignkey
    "rating" - charfield - 1-5 stars

# Order checkout Model
     order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')



# Font/Typeface
    Poppins - Googlefonts
