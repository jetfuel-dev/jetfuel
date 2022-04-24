<p align="center">
<br><br><br>
<a href="https://github.com/mocha-dev/mocha"><img src="https://raw.githubusercontent.com/mocha-dev/mocha/main/assets/mocha.png" alt="Mocha logo: Mocha is the Python Performance Profiler for Production" width="200px"></a>
<br><br>
</p>

<p align="center">
<b>Python Performance Profiling for Production</b><br>
<b>~ It's About Time ~</b>
</p>

Mocha is a Python performance profiler that can monitor your entire deployment in production, and makes results easy to aggregate and search through.

Bad code performance is often a result of lack of visibility, with [real world consequences](https://uxplanet.org/how-page-speed-affects-web-user-experience-83b6d6b1d7d7). Mocha can help you monitor performance over time.

<br>
<p align="center">
<b>What gets measured gets managed!</b>
</p>
<br>

Useful for Profiling:

- 🌎 API performance
- 🚀 CI/CD granular performance
- 💡 ML training & inference
- 📀 Database queries
- 📊 Data pipelines / compute jobs

<br>

## Installation

```bash
pip install mocha-time
```

## Start / Stop

```python
import mocha

mocha.init(url="http://localhost:9000")

p = mocha.start("ML Training")

import time
time.sleep(10)

p.stop()
```

## Profiler

```python
import mocha

mocha.init(url="http://localhost:9000")

with mocha.Profiler("ML Training"):

    import time
    time.sleep(10)
```

## Decorator

```python
import mocha

mocha.init(url="http://localhost:9000")

@mocha.profiler("ML Training")
def ml_training():

    import time
    time.sleep(10)
```
