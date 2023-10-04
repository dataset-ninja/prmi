Dataset **PRMI** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/J/r/vp/57CGXVP1ZGkAdM9O44W6Ep0mjXUtatHYJCMAGBFp1KdzYKhlHNXfzrZjhotWkAIm1Q2od4DsFEZimXQ6Ztk6tgj9HCPezZYY8nejpM872LWn6v8PfeLF0Od2JkI1.tar)

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
