<p align="center">
<br><br><br>
<a href="https://github.com/mocha-dev/mocha"><img src="https://raw.githubusercontent.com/mocha-dev/mocha/main/assets/mocha.png" alt="Mocha logo: Mocha is the Python Performance Profiler for Production" width="200px"></a>
<br><br>
</p>

<p align="center">
<b>Python Performance Profiling for Production</b><br>
<b>~ It's About Time ~</b>
</p>

Mocha is a performance profiler that can monitor the performance of your production Python, and makes results easy to aggregate and search through.

Mocha is designed for **Purposeful Profiling**. This means that you only use Mocha around code of interest, instead of dumping all code performance logs and mining it later.

Useful for Profiling:

- 🌎 API performance
- 🚀 CI/CD stage / granular performance
- 💡 ML training & inference jobs
- 📀 Database queries
- 📊 Data pipelines / compute jobs

<br>
<p align="center">
<b>What gets measured gets managed!</b>
</p>
<br>

<p align="center">
<img src="https://raw.githubusercontent.com/mocha-dev/mocha/main/assets/continuous_profiling.png" alt="Mocha logo: Mocha is the Python Performance Profiler for Production" width="600px">
</p>

![Dashboard](https://raw.githubusercontent.com/mocha-dev/mocha/main/assets/dashboard.png)

Bad performance has [real world consequences](https://uxplanet.org/how-page-speed-affects-web-user-experience-83b6d6b1d7d7), and is often a result of **lack of visibility**, *even if you are logging it, if it's not be easy to get to, it will be ignored*.

<br>

## Installation

```bash
pip install mocha-time
```

```bash
docker run -p 9000:9000 mochadev/mocha
```

## Demo

```python
import mocha

mocha.init(url="http://localhost:9000")

mocha.demo()
```

## Usage

```python
# Start / Stop
p = mocha.start("Foobar")

pass

p.stop()

# Profiler
with mocha.Profiler("Foobar"):
    pass

# Function Decorator
@mocha.profiler("Foobar")
def ml_training():
    pass
```
