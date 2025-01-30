Dataset **PRMI** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzI0NDNfUFJNSS9wcm1pLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIkZtV3c3UUtSYjlub1BlVWIva29YYU5aZWlUZXpmVjZBUzlnS2VzZXBPaG89In0=)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='PRMI', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [PRMI_official.zip](https://zenodo.org/record/5974905/files/PRMI_official.zip?download=1)
- [README](https://zenodo.org/record/5974905/files/README?download=1)
