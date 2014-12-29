<% if (@wlhost and @wlport and @wluser and @wlpass) -%>
instance = "t3://<%= @wlhost %>:<%= @wlport %>"
connect ('<%= wluser %>','<%= wlpass %>',instance)
serverRuntime()

metrics = [
<%- @metrics.each do |metric| -%> 
("<%= metric[0] %>","<%= metric[1] %>","<%= metric[2] %>"),
<%- end -%>
]

for mbeanpath, graphitestat, mbeanname in metrics:
    cd(mbeanpath)
    print "%s:%s:%s:%i" % ("metric", graphitestat, mbeanname, get(mbeanname))

<% else -%>

<%= @wluser %>
<%= @wlhost %>
<%= @wlport %>
<%= @wlpass %>
# insufficient configuration to generate beans.py from puppet

<% end -%>
