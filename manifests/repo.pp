class diamond::repo {

  include apt

  apt::ppa { 'ppa:liquidgecka/graphite': }

}
