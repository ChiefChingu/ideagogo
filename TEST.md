# Test document

Back to the [README](https://github.com/ChiefChingu/ideagogo/blob/master/README.md).

First I tested the project with the validators for css and markup. Then I manually tested all user stories and features (if relevant). All results are displayed below. The last section goes into more detail about the issues I encountered.

## W3C CSS Validation Service
Directly inputting the project URL into the validators causes errors that are bugged. For instance:
```
Value Error : margin Unknown dimension 1rem
```
Of course this is not right. The validator gives around 300 of such errors. To overcome this I have copied the CSS from my custom stylesheet. And ran this in the validator tool. The result is perfectly fine code.

Note that I did not bother to check the materialize CSS.

## W3C Markup Validation Service
Many errors resulting from customizing materializecss components. After fixing these, no errors or warnings were shown.
vali
### JSHint
#### email.js
- Undefined variable: ```emailjs``` (lines 3 and 22). This is out of my control, I use the EmailJS code as per instruction. 
- Unexpected use of '|' (line 21). Again out of my control, I use the EmailJS code as per instruction.

### app.js
- One warning: Do not use 'new' for side effects (line 19). Solved this by storing it in a var mobile.
- Warning is gone, but now there is a mention of an unused variable...

