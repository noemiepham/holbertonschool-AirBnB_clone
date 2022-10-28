# AirBnB clone - Web static

-   Novice
-   By:  Guillaume
-   Weight:  1

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2021/9/135ef103cf7ed150c9760aadc66844113dfc3d35.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221026%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221026T040912Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4d6975ea788f3cc27caec12102aa0461f63476af24b60c1e4803a5a81bb8574c)

## Background Context

### Web static, what?

Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

-   Create simple HTML static pages
-   Style guide
-   Fake contents
-   No Javascript
-   No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository  `AirBnB_clone`  from your partner if you were not the owner of the previous project.

## Resources

**Read or watch**:

-   [Learn to Code HTML & CSS](https://intranet.hbtn.io/rltoken/9P868D9X6hKF-iPeuTjUMA "Learn to Code HTML & CSS")  (_until “Creating Lists” included_)
-   [Inline Styles in HTML](https://intranet.hbtn.io/rltoken/3w80rVNNceP13m7D52ma3Q "Inline Styles in HTML")
-   [Specifics on CSS Specificity](https://intranet.hbtn.io/rltoken/miNTDX58opEBx0EbOWPySw "Specifics on CSS Specificity")
-   [CSS SpeciFishity](https://intranet.hbtn.io/rltoken/JYH8gnHJXb7aF-y4xwFW4A "CSS SpeciFishity")
-   [Introduction to HTML](https://intranet.hbtn.io/rltoken/Jrc0YlYYAry_aRJBZB5v2Q "Introduction to HTML")
-   [CSS](https://intranet.hbtn.io/rltoken/mq0A1qZJs8J0SE5xyxODzg "CSS")
-   [MDN](https://intranet.hbtn.io/rltoken/8AWCJcUwO2UK5FFUb7G-iw "MDN")
-   [center boxes](https://intranet.hbtn.io/rltoken/CWYMpBgaImw4SPgfibG2eQ "center boxes")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/jTzHi5Wsmr55wY99p7gAFQ "explain to anyone"),  **without the help of Google**:

### General

-   What is HTML
-   How to create an HTML page
-   What is a markup language
-   What is the DOM
-   What is an element / tag
-   What is an attribute
-   How does the browser load a webpage
-   What is CSS
-   How to add style to an element
-   What is a class
-   What is a selector
-   How to compute CSS Specificity Value
-   What are Box properties in CSS

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files should end with a new line
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should be W3C compliant and validate with  [W3C-Validator](https://intranet.hbtn.io/rltoken/cg3av28O6YAI9vZApf3zHg "W3C-Validator")
-   All your CSS files should be in  `styles`  folder
-   All your images should be in  `images`  folder
-   You are not allowed to use  `!important`  and  `id`  (`#...`  in the CSS file)
-   You are not allowed to use tags  `img`,  `embed`  and  `iframe`
-   You are not allowed to use Javascript
-   Current screenshots have been done on  `Chrome 56`  or more.
-   No cross browsers
-   You have to follow all requirements but some  `margin`/`padding`  are missing - you should try to fit as much as you can to screenshots

## More Info

![alt text](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png)





### Full details

#advanced

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on  `8-index.html`)

Add more information to a Place  `article`:

-   List of Amenities:
    -   tag  `div`
    -   classname  `amenities`
    -   margin top 40px
    -   contains:
        -   title:
            -   tag  `h2`
            -   text  `Amenities`
            -   font size 16px
            -   border bottom #DDDDDD 1px
        -   list of amenities:
            -   tag  `ul`  /  `li`
            -   no list style
            -   icons on the left:  [Pet friendly](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_pets.png "Pet friendly"),  [TV](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_tv.png "TV"),  [Wifi](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_wifi.png "Wifi"), etc… feel free to add more
-   List of Reviews:
    -   tag  `div`
    -   classname  `reviews`
    -   margin top 40px
    -   contains:
        -   title:
            -   tag  `h2`
            -   text  `Reviews`
            -   font size 16px
            -   border bottom #DDDDDD 1px
        -   list of review:
            -   tag  `ul`  /  `li`
            -   no list style
            -   a review is described by:
                -   `h3`  tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
                -   `p`  tag for the text (font size 12px)

Requirements:

-   You must use:  `header`,  `footer`,  `section`,  `article`,  `button`,  `h1`,  `h2`,  `h3`,  `h4`,  `ul`,  `li`  tags
-   No inline style
-   You are not allowed to use the  `img`  tag
-   You are not allowed to use the  `style`  tag in the  `head`  tag
-   All images must be stored in the  `images`  folder
-   You must have 5 CSS files:
    -   `styles/4-common.css`: for the global style (`body`  and  `.container`  styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style
    -   `styles/6-filters.css`: for the filters style
    -   `styles/100-places.css`: for the places style

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/0e0e57ed2baf9239cc87000a5f81b54011a924e9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221028T040939Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=32ce32665754e532af616faa05e937101bb4cacf1f310dd473ad8ff1f45af45b)

**Repo:**

-   GitHub repository:  `holbertonschool-AirBnB_clone`
-   Directory:  `web_static`
-   File:  `100-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/100-places.css, images/`