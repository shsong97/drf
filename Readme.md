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

git remote add origin GITURL
git push origin master