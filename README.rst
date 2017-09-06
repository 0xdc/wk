wk
====

Quick start
-----------

1. Add "wk" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'wk',
    ]

2. Include the wk URLconf in your project urls.py like this::

    url(r'^.well-known/', include('wk.urls')),

3. Run `python manage.py migrate` to create the wk models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/.well-known/ to view templates.
