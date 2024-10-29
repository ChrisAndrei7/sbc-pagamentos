#!/bin/bash
foi i in {1..1000}; do
  curl localhost:31000/vendas
  sleep $1
  done