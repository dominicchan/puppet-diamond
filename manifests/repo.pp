class diamond::repo {



case $::osfamily {
   'redhat': {
     yumrepo { "diamond" :
       descr => "Diamond, a graphite linux agent",
       baseurl => "http://download.linuxdataflow.org:81/rpm-repos/diamond/el${operatingsystemmajrelease}/",
       enabled => 1,
       gpgcheck => 0,
       gpgkey => absent,
       exclude => absent,
       metadata_expire => absent,
     } 
   }
   'debian': {
     include apt
     apt::ppa { 'ppa:liquidgecka/graphite': }
   }
}




}
