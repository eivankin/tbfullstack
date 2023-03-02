#!/bin/sh

ROOT_DIR=/usr/share/nginx/html

# Replace env vars in JavaScript files
echo "Replacing env constants in JS"
for file in $ROOT_DIR/assets/*.js;
do
  echo "Processing $file ...";

  sed -i 's|VITE_API_ENTRYPOINT|'${VITE_API_ENTRYPOINT}'|g' $file

done

echo "Starting Nginx"
nginx -g 'daemon off;'
