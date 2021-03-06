#!/usr/bin/env bash

composer install --no-dev
php artisan env:set production -n --env local
php artisan key:generate -n --env local
php artisan migrate --seed --force
npm install
npm run production
