# final-year-project

## Things to do
1.will add options to output results to csv file to summary results


## Pretty Print Json to terminal
python -m json.tool input.json

cat input.json | jq '.'

## Show all paths in json
[links](https://github.com/stedolan/jq/issues/243)

jq -c 'path(..)|[.[]|tostring]|join("/")' banners_test.json

jq 'path(..)' banners_test.json
