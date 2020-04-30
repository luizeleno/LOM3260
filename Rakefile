desc "Build jekyll - production"
task :build do
  puts "\n## Buildind jekyll on production environment"
  status = system("JEKYLL_ENV=production bundle exec jekyll build")
  puts status ? "Success" : "Failed"
end

desc "Build jekyll - development"
task :build_dev do
  puts "\n## Buildind jekyll on development environment"
  status = system("bundle exec jekyll build")
  puts status ? "Success" : "Failed"
end

desc "Commit _site/"
task :commit do
  puts "\n## Staging modified files"
  status = system("git add -A")
  puts status ? "Success" : "Failed"
  puts "\n## Committing a site build at #{Time.now.utc}"
  message = "Build site at #{Time.now.utc}"
  status = system("git commit -m \"#{message}\"")
  puts status ? "Success" : "Failed"
  puts "\n## Pushing commits to remote"
  status = system("git push origin master")
  puts status ? "Success" : "Failed"
end
