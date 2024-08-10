# Introduction to Back-End Development
## Module 1: Get started with web development
1. HTML, CSS, JavaScript
2. page rendering
3. web hosting
    1. shared hosting: several websites on one physical server.
    2. virtual private surface (VPS) hosting : several VPS instances (VM) separate from one physical server.
    3. dedicated hosting: physical server dedicated to one website only.
    4. cloud hosting: a combination of physical and virtual servers.
4. IP addresses
5. Network packet / Data packet
6. Transmission Control Protocol (TCP): for data that must arrive correctly and in order
7. User Datagram Protocol (UDP): has the potential to lose data, but you’ll have much higher speeds in return
8. HTTP
    1. makeup: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#http_messages
    2. responses status: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
9. HTML:  structure and content; CSS: format and style; JavaScript: core function and interactivity
10. web browser developer tools
    1. elements: inspect the documents, HTML elements and properties
    2. console: JavaScript logs.
    3. sources: content resolved for the current page.
    4. network: timeline and details of HTTP requests and responses.
    5. performance: shows what the web browser is doing over time
    6. memory: resource consuming
11. library: reusable pieces of code; frameworks: a structure for developers to build with.
12. Application Programming Interface (API): known as gateways or middleware
    1. Web APIs / Browser APIs: browsers' built-in APIs
    2. RESTful API/ REST API: a web server that provides responses to requests.
    3. Sensor-Based API: what IOT base on


## Module 2: Introduction to HTML5 and CSS
1. opening tag: `<p>`, closing tag: `</p>`, self-closing: `<br>` or `<br/>` 
2. HTML documents structure
```html
<!DOCTYPE html>
<!-- this is a comment in html -->
<html>
    <head>
    <!-- inside a head won't displayed in a webpage, is for web info or metadata -->
        <title> TitleName </title>
        <!-- this title string will display in the web browser tab -->
        <!-- you can also link a CSS in head -->
    </head>

    <body>
    <h1> MainHeading </h1>
    <h2> SubHeading </h2>
    <p> Paragraph </p>
    <p>
        LineBreak<br>
        <!-- you can style <strong> with CSS -->
        <strong>Strong</strong> 
        <!-- in the material: "Bold tags should be used to draw attention but not to indicate that something is more important." -->
        <!-- someone on stackoverflow says you should stop using <b>, styling in CSS instead -->
        <b>Bold</b>
        <!-- similar to <strong> -->
        <em>Emphasis</em>
        <!-- in the material: "Italics represent off-set text and should be used for technical terms, titles, a thought or a phrase from another language." -->
        <i>Italics</i>
        <s>Strikethrough</s>
        <del>Delete</del>

        <!-- anchor tag <a>: for linking documents -->
        <!-- href: hypertext reference --> 
        <a href = "fileName.html" >linkTitle</a>
        <!-- image tag <img>: for adding images -->
        <!-- source<src>,  alternative text<alt> -->
        <!-- <alt> will not displayed on the site -->
        <img src = "imageName.jpeg" width="240" height="135" alt="imageDescription" >
    </body>
</html>
```

3. List, Table and
```html
<!-- List -->
<ul>
    <li>Unorder</li>
    <li>List</li>
</ul>
<ol>
    <li>Order</li>
    <li>List</li>
<ol>


<!-- Table -->
<table>
    <!-- tr: table row -->
    <tr>
    <th>tableHead1</th>
    <th>tableHead1</th>
    </tr>
    <tr>
    <td>tableData1</td>
    <td>tableData2</td>
    </tr>
</table>
<div>DivisionOrSection</div>
```

4. Form
```html
<!-- http methods GET or POST -->
<form action="pathOrURL" method="GET">
    <label for="userName">Username:</label><br>
    <!-- input type=text is only for single line -->
    <input type="text" name="userName" />
    

    <!-- more input type -->
    <input type="password" /> <!-- this will mask the input text -->
    <input type="submit" /> <!-- submit button -->

    <input type="checkbox" name="name" value="value" />
    <label for="name" >The string after the check box.</label><br/>

    <input type="radio" /> <!-- like checkbox, but only one can be check -->

    <input type="number" />
    <input type="email" />
    <input type="file" />

    <!-- multi line text area-->
    <textarea name="multiLine" rows="5"></textarea>

    <!-- drop-down list -->
    <select name="food">
        <option value="optionOne">OptionOne</option>
    </select>
</form>
```

5. **Document object model (DOM)**: represents the HTML document element in a tree structure so that they can be used and modified by JavaScript.
6. Web accessibility: https://www.w3.org/TR/html-aria/
7. CSS syntax
```css
/* this is a comment in css */
/* set all <h1> color to grey */
h1 { 
    /* h1 is a Element Selectors */
    /* inside "{}" call declaration block */
    color: grey;
    /* color is a property
    grey is a value of a property */
}

#latest {
    /* "#" is for ID Selectors, apply to id="latest" */
    background-color: purple;
}

.navigation { 
    /* "." is for Class Selectors, apply to class="navigation" */
  margin: 2px;
}

p.introduction { 
    /* Element with Class Selector */
  margin: 2px;
}
```

8. Descendant Selectors and Child Selectors
```html
<div id="blog">
    <h1>Latest News</h1>
    <div>
        <h1>Today's Weather</h1>
        <p>The weather will be sunny</p>
    </div>
    <h1>More News</h1>
    <p>Subscribe for more news</p>
</div>
<div>
    <h1>Archives</h1>
</div>
```
```css
/* Descendant Selectors */
/* select all h1 elements that are contained within the id="blog", will not select "Archives" */
#blog h1 {
  color: blue;
}
/* can have multiple descendant */
#blog div h1 {
  color: blue;
}

/* Child Selectors */
/* select only one level of h1 within the id="blog" */
/* will select "Latest News" and "More News", but not "Today's Weather" */
#blog > h1 {
  color: blue;
}
```

9. A special keyword called a **pseudo-class** allows developers to select elements based on their state.
    - https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_pseudo-elements
10. install VS code extension Live Preview to see html change immediately.
11. link a CSS to HTML
```html
<head>
<!-- inside a head won't displayed in a webpage, is for web info or metadata -->
    <title> TitleName </title>
    <link rel="stylesheet" href="styleSheetName.css" />
</head>
<body>
```
12. CSS color: RGB, HEX, HSL, RGBA, HSLA values, and predefined color names: 
    - https://www.w3schools.com/css/css_colors.asp
13. CSS text:
    1. font-family (sets a prioritized list of one or more font, incase some font is not available): 
    https://developer.mozilla.org/en-US/docs/Web/CSS/font-family
    2. size: https://developer.mozilla.org/en-US/docs/Web/CSS/font-size
    3. text-transform (specifies how to capitalize an element's text): https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform
    4. text-decoration (sets the appearance of decorative lines on text): https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration

14. Box model
    1. https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model
    2. content > padding > border > margin
    3. `content`: https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Sizing_items_in_CSS
        - (`min-`/`max-`)`height`, (`min-`/`max-`)`width`
    4. `padding`: https://developer.mozilla.org/en-US/docs/Web/CSS/padding
        - `-top`, `-right`, `-bottom`, `-left`
    5. `border`: https://developer.mozilla.org/en-US/docs/Web/CSS/border
        - `-top`(`-width`, `-style`, `-color`), `-right`(`-width`, `-style`, `-color`), `-bottom`(...), `-left`(...), `-width`, `-style`, `-color`
    6. `margin`: https://developer.mozilla.org/en-US/docs/Web/CSS/margin
        - `-top`, `-right`, `-bottom`, `-left`
    7. shorthand properties: https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties

15. Document flow: Every HTML element has a default display value. 
    1. A block-level element always starts on a new line. like: `<div>` `<h1>`
    2. An inline element does not start on a new line. like: `<a>` `<img>`
    3. default display value can be change in CSS: https://developer.mozilla.org/en-US/docs/Web/CSS/display 
16. Alignment basics
    1. `text-align:` https://developer.mozilla.org/en-US/docs/Web/CSS/text-align
    2. element alignment with box model: https://www.w3schools.com/css/css_align.asp
    - `position`, `float`

## Module 3: UI Frameworks
## Module 4: Graded Assessment