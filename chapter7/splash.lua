function main(splash, args)
    splash:go("https://www.baidu,com")
    splash:wait(0.5)
    local title = splash:evaljs("document.title")
    return {title=title}
end

function main(splash, args)
    local example_urls = {"www.baidu.com", "www.taobao.com", "www.zhihu.com"}
    local urls = args.urls or example_urls
    local results = {}
    for index, url in ipairs(urls) do
        local ok, reason = splash:go("https://" .. url)
        if ok then
            splash:wait(2)
            results[url] = splash:png()
        end
    end
    return results
end