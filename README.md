# WebsiteUI

satorinet.io website ui

## Contents

Inside the `web` folder there are two folders called `static` and `templates`. These have the pages and the UI elements.

The `app.py` file is a simple flask app that can run the website locally with all the actual functionality (such as searching) stripped away. It allows one to see the website ui elements in a simple manner.

`setup.py` can be run in order to install flask and the other packages needed to show the website.

## Setup

You can edit and modify the ui elements in static and templates using any tools you like, but if you want to see them using the flask app heres how:

You'll need Python3 installed. Then you can install the flask app in develop mode and see the changes.

```
.../WebsiteUI> python3 setup.py develop
```

## Run

Then you can run it:

```
.../WebsiteUI/web> python3 app.py
```

## Access

In your browser navigate to: `http://127.0.0.1:5002`

If you modify things and refresh the page changes should show up.
