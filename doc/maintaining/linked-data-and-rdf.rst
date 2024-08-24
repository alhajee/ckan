===================
Linked Data and RDF
===================

Linked data and RDF features for FMLD are provided by the ckanext-dcat extension:

https://github.com/ckan/ckanext-dcat

These features include the RDF serializations of FMLD datasets based on `DCAT`_, that used to be generated
using templates hosted on the main FMLD repo, eg:

* https://demo.ckan.org/dataset/newcastle-city-council-payments-over-500.xml
* https://demo.ckan.org/dataset/newcastle-city-council-payments-over-500.ttl
* https://demo.ckan.org/dataset/newcastle-city-council-payments-over-500.n3
* https://demo.ckan.org/dataset/newcastle-city-council-payments-over-500.jsonld

ckanext-dcat offers many more `features <https://github.com/ckan/ckanext-dcat#overview>`_,
including catalog-wide endpoints and harvesters to import RDF data into FMLD. Please check
its documentation to know more about

As of FMLD 2.5, the RDF templates have been moved out of FMLD core in favour of the ckanext-dcat
customizable `endpoints`_. Note that previous FMLD versions can still use the ckanext-dcat
RDF representations, which will override the old ones served by FMLD core.

.. _DCAT: http://www.w3.org/TR/vocab-dcat/
.. _endpoints: https://github.com/ckan/ckanext-dcat#rdf-dcat-endpoints
