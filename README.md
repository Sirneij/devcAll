# Devc

**NOTE**: Exposing some secret details in the `settings.py` file was delibrate!

[sirneijblog.herokuapp.com](https://sirneijblog.herokuapp.com) is a complex web application inspired by `Frances Nnamadim`, a senior and regular colleague who worked as a Business Analyst and UI/UX designer in `ipNX Nigeria Ltd's` department of Business Intel­ligence and Data Analytics (BIDA). It is `blogging` and `portfolio` application fully implemented in `Django` frame­work with `PostgreSQL` database at the back­end and some bits of `Ajax` for better user experiences. Utilizing the free `HTML` template oferred by [Styleshout](https://www.styleshout.com/), [sirneijblog.herokuapp.com](https://sirneijblog.herokuapp.com) was built with three (3) other main applications embedded, each embedding other systems in turn:

- **Account management system**: This application provides interfaces for users
  authentication and authorization. It allows direct authentication from popular social
  and technical websites such as `Facebook`, `Twitter` and `Github` among others as shown
  in below:
  ![Sirneijblog Login and Signup](https://github.com/sirneij/devcAll/blob/master/devcsignup.png?raw=true)

- **Blogging system**: This is the heart of the overall system. It controls `user’s posts` - their `creation` and `update`, with a `rich text editor` and advanced text formatting sys­
  tem; and posts’ `deletion` - ­profiles and portfolio with various mini­-systems such as
  `full­text search engine`, `tagging`, `related­ posts recommendation`, `asynchronous threaded comment­ing` and `slack­-like chatting(yet to be rolled out)` systems, embedded. Users’ posts could also be `liked` and
  shared asynchronously`.

- **Portfolio system**: This serves as an extension of the account management sys­
  tem where authors of post(s) showcase their skills to their potential recruiters. It
  structures authors profiles, education, skills, projects and recommendations accord­
  ingly which can be downloaded in Portable Document Format (PDF)
