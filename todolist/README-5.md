# Tugas 5

## Inline, Internal, and External CSS

CSS can be written as an inline, internal, or external. Inline CSS are basically CSS that is written directly on a particular element. This way of writing CSS is nice if you wanted to make slight changes just for a certain element, but it's commonly discouraged since the styles that you write for a certain element would not be repeatable (you would have to do it for every element). For example:
```html
<div style="width: 100vw; height: 100vh; ...">nyehehe</div>
```
Internal CSS is a way to write CSS that applies to one particular page. This is done by using the `<style>` tag which will contain CSS styles. This way of writing CSS would only apply for a single page in your application, which is one of it's drawbacks. But sometimes you might want to style just a single page, by using internal css, you would not be required to create another CSS file. For example:
```html
<style>
    .kekw {
        color: palegoldenrod;
        ...
    }
</style>
```
External CSS is a CSS that is written inside another CSS file format `.css`. For a page to access that file, you need to reference it by using the `<link>` tag. This way of writing code is inherently the most structured. By having each files being just what they are, it would help with debugging and much more. One drawback to this is that external CSS takes a while to load. For example:
`styles.css`
```css
body {
    margin: 0;
    padding: 0;
}
```
`index.html`
```html
...
<link rel="stylesheet" href="styles.css" type="text/css">
...
```

# HTML Tags

- `<div>`, a block element that defines a division
- `<h1-6>`, a block element that defines HTML headings.
- `<p>`, defines a paragraph element
- `<a>`, anchor tag that creates hyperlink
- `<input>`, receives input from user
- `<footer>`, HTML semantic that defines the footer of a page
- and more ...

# CSS Selectors

- `*`, selects everything
- `.kekw`, a class selector (selects all elements with the class `kekw`)
- `#kekw`, an ID selector (selects all elements with the ID `kekw`
- `body`, a group selector (selects all elements with the appropriate tag)
- `::before`, gives content before the referenced element
- and more ...

# Implementation

First I imported bootstrap to use some of their components and then expand as well as customize them later on. To import boostrap, I just needed to include the CDN they provide to my `base.html` and that's it. I used accordions instead of cards for this one, and then I used GSAP to give a staggering effect everytime you scroll through each accordion. For the media query, I only used it for the navbar. If it gets too small, without media query, the nav-items are not centered, so I used flex to center them.

