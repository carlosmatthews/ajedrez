#!/usr/bin/env bash

cd frontend
npm run build
cd ..
git push heroku heroku:master