## 설정
<pre><code>
virtualenv myworkon
cd myworkon/bin
activate

pip install django
pip install djangorestframework
pip install markdown
pip install django-filter

git init
git add .
git commit -am "initial update"

git config --global user.name "shosng97"
git config --global user.email "shsong97@gmail.com"

git remote add origin https://github.com/shsong97/drf.git
git push -u origin master

pip freeze > requirements.txt
</code></pre>