
  

# Welcome to Arman Behnam Projects!!

  

  

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

  

[![](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

  

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/ArmanBehnam)

  

[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/ArmanBehnam)

 
  

  

## Table of contents

  

  

*  [About](#about)

  

*  [Technologies Used](#technologies-used)

  

*  [Results of the Project](#results-of-the-project)

  

*  [Installation](#installation)
  

*  [License](#license)

  

  

## About


#### Neighborhood
>A district or community within a town or city.
  
#### Manhattan

> Manhattan is a major central city for diversity since many people from different cultural atmospheres have brought their families and dreams to Manhattan. 

>The city has consistently seen people from around the world move to the city and call it home. It has been a center for trade and economic growth. 

>Manhattan is known world wide as a cultural melting pot. While other states have had immigration surges, none have compared to the diversity and sheer number of immigrants that have made their way to the City. 

>So these number of varies cultures combined to create a great diversity for itself. Since People from all over the world tend to come up here, we can see some many of their cultural aspects Transport, Food, Clothing, and so on…  


#### Problem Description

>Restaurant is a place where people come to have food and drinks for a cost, People love to do many things and try something new or stick with their own routines, it depends on the individual and there are so many of them with different cultural and various aspects in Manhattan. 

>There are so many cuisines, which is based on the style of cooking, the ingredients, dishes and techniques. For our problem let's stick with Indian cuisine.

>Let’s assume in this one of the world’s most diverse region we want to open an Indian restaurant, so what are all the factors we have to take into account such as follows,
* Market Places
* Competition in particular location
* Aiding places that make people come to restaurants like Gym,  * Entertaining Public places
* Population
* Menu from competitors

>And so on… So our solution needs to be data driven for avoiding or considering low risk criteria and high success rate and thus apply our overall knowledge in the techniques and the tools gained so far in this course.


### **`Note`**
> Here addresses of locations converted into their equivalent `latitude` and `longitude` values and also used `Foursquare API` is used to explore the `neighborhoods` in `Manhattan City`.

## Technologies Used

  

> [![](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) is used as Programming Language.

  

> `Numpy` and `Pandas` is used to analysis and manipulation of data.

> `Matplotlib`  visualisation of `maps`.
  
 > `request` and `json` packages are used to get the data from `Foursquare API` and to convert the received data in json format for the ease of work.

> `geopy` packages is used to get `coordinates` using the location that we got from the GET request.

> Using the `folium` package to visualise the map of `New York City` and mainly `Manhattan`, also it is see the map of different clusters that we got from the `machine learning model`.

> `Sciki-learn` is used for data preprocessing, creating machine learning model and evaluating it, thus creating a pipeline.

 
> `Pipenv` is the virtual environment used for the project. `Jupyter Notebook` is used to for the entire data science and machine learning life cycle.

  

## Results of the Project

  

#### New York Map

![New York](https://github.com/AkashSDas/Battle-of-Neighborhoods-in-Manhattan/blob/master/project-results-images/New-York.png)

#### Manhattan Map

![Manhattan](https://github.com/AkashSDas/Battle-of-Neighborhoods-in-Manhattan/blob/master/project-results-images/Manhattan.png)

#### Manhattan Cluster Map

![Manhattan Cluster](https://github.com/AkashSDas/Battle-of-Neighborhoods-in-Manhattan/blob/master/project-results-images/Manhattan-Cluster.png)


## Installation

  

  

It is highly **recommended** to use **`virtual enviroment`** for this project to avoid any issues related to dependencies.

  

  

Here **`pipenv`** is used for this project.

  

  

There is a **`requirements.txt`** file in `'Battle-of-Neighborhoods-in-Manhattan'/requirements.txt` which has all the dependencies for this project.

  

  

- First, start by closing the repository

  

  

```bash
git clone https://github.com/AkashSDas/Battle-of-Neighborhoods-in-Manhattan
```

  

  

- Start by installing **`pipenv`** if you don't have it

  

```bash
pip install pipenv
```

  

  

- Once installed, access the venv folder inside the project folder

  

```bash
cd  'Battle-of-Neighborhoods-in-Manhattan'/venv/
```

  

  

- Create the virtual environment

  

```bash
pipenv install
```

  

The **Pipfile** of the project must be for creating replicating project's virtual enviroment.

  

  

This will install all the dependencies and create a **Pipfile.lock** (this should not be altered).

  

  

- Enable the virtual environment

  

```bash
pipenv shell
```

  

  

- dataset, jupyter notebook and model are in `'Battle-of-Neighborhoods-in-Manhattan'/venv/src` folder.

  

  

```bash
cd src/
```

  

  

- To start/view the jupyter notebook

  

```bash
jupyter noterbook
```

  

  

This will open a webpage in the browser from there you can click on notebook.ipynb to view it.

  

  

## License

  

  

This project is licensed under the MIT License - see the [MIT LICENSE](LICENSE) file for details.
