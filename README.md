Search bar icon inside input on the right helped by Slack London community

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


# Products Model
"pk" - Primary key
"model" = products.product
"fields" = 
    "category" - Product category ForeignKey
    "sku" - product sku
    "name" - product name
    "description" - product description
    "price" - product price
    "rating" - product rating
    "image" - product image

# Category Model
    "name" - category name PrimaryKey
    "friendly_name" - friendly name for front end
