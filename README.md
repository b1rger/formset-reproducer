formset reproducer

contains an `Index` view on `/` that shows a button for a form dialog. The
button includes the form from `/form` into the dialog using htmx.

If the DOM on the index page contains a `Selectize` dropdown, the dropdown in
the htmx-included form uses `Selectize`. If the DOM does **not** contain a
`Selectize` dropdown, the dropdown in the htmx-included form does not get
"selectized".
