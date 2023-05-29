### CS50 Shirtificate
John Harvard's CS50 Shirtificate

Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an **[I took CS50](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt)** t-shirt, **[shirtificate.png](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png)**, customized with a user’s own name.

In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using **[fpdf2](https://pypi.org/project/fpdf2/)**, a CS50 shirtificate in a file called shirtificate.pdf similar to **[this one for John Harvard](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/jharvard.pdf)**, with these specifications:

- The [orientation](https://pyfpdf.github.io/fpdf2/PageFormatAndOrientation.html) of the PDF should be Portrait.
- The [format](https://pyfpdf.github.io/fpdf2/PageFormatAndOrientation.html) of the PDF should be A4, which is 210mm wide by 297mm tall.
- The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
- The shirt’s [image](https://pyfpdf.github.io/fpdf2/Images.html) should be centered horizontally.
- The user’s name should be on top of the shirt, in white [text](https://pyfpdf.github.io/fpdf2/TextStyling.html).

All other details we leave to you. You’re even welcome to add borders, colors, and [lines](https://pyfpdf.github.io/fpdf2/Shapes.html#lines). Your shirtificate needn’t match John Harvard’s precisely. And no need to - wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s [tutorial](https://pyfpdf.github.io/fpdf2/Tutorial.html) to learn how to use it. Then skim fpdf2’s API (application programming interface) to see all of its functions and parameters therefor.

No need to submit any PDFs with your code. But, if you would like, you’re welcome (but not expected) to share a shirtificate with your name on it in any of CS50’s communities!
![image](https://github.com/jwattspajaro/CS50-s/assets/18930760/9d7f6127-745f-41f4-9c44-7e73f3da3cf4)


#### Hints
- Note that fpdf2 comes with a class called FPDF, which has quite a few methods, per https://pyfpdf.github.io/fpdf2/fpdf/#fpdf.FPDF. You can install it with:
pip install fpdf2
- Note that you can extend FPDF and instantiate your own subclass thereof in order to add a header to every page of a PDF, per https://pyfpdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image. Or you can add it as text yourself.
- Note that you can disable automatic page breaks, which might otherwise cause your PDF to overflow from one page to two, with set_auto_page_break, per https://pyfpdf.github.io/fpdf2/Margins.html.
- Note that a cell’s height can be negative, to move it upward.
You can open shirtificate.pdf, once outputted, by clicking it in VS Code’s file explorer.

