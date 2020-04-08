import rshanker779_common as utils
import pytest
import requests as r


def test_format_header_string():
    headers = """
    GET / HTTP/1.1
    Host: www.bbc.co.uk
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Language: en-GB,en;q=0.5
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Cookie: ckns_explicit=1; ckns_sa_labels_persist={}; ckns_privacy=july2019; ckns_id=eyJkbiI6InJvdmluZ3JvdmVyIiwiYWIiOiJvMTgiLCJwYSI6IkNNOCIsImVwIjp0cnVlLCJldiI6dHJ1ZSwicGwiOmZhbHNlLCJwcyI6InhFV3dTbFRfTHJrNDVOMm9nWnpYckRXSVFCaWEweWFMcS0xYzR3V2x4U3ciLCJjbCI6ZmFsc2UsInNlcy1leHAiOjE1NzA3MTUyODIwMDAsImp3dC1leHAiOjE2MzM3ODYzODIwMDAsInJ0a24tZXhwIjoxNjMzNzg2MzgyMDAwLCJ0a24tZXhwIjoxNTg2MTY4MTU1MDAwfQ; ckns_stateless=1; ckns_sylphid=Den1nwf59VxWE4IjrVZSoX4wYOaHmkKfNAV6aCwpE0g; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22b79fb0f0-9d9e-4442-b1e4-248a9e2aa82a%22%2C%22options%22%3A%7B%22end%22%3A%222020-12-06T20%3A34%3A03.465Z%22%2C%22path%22%3A%22%2F%22%7D%7D; ckns_policy=000; ckns_policy_exp=1611081053599; ckns_pgAgeConfirm=true; ckns_bbcTvVod=true; ckns_mvt=d482285d-5a61-4a1e-bee1-84046473edac; ckns_orb_fig_cache={%22ad%22:0%2C%22ap%22:0%2C%22ck%22:1%2C%22eu%22:1%2C%22uk%22:1}; ecos.dt=1586133182864; ckns_nonce=_6-EAPVmOLMjF7WutnoHZt6u; ckns_atkn=eyJ0eXAiOiJKV1QiLCJ6aXAiOiJOT05FIiwia2lkIjoiRWdVVSs4TmhhQVlLYzZ5bG9DQnJuS1BUY2U4PSIsImFsZyI6IkVTMjU2In0.eyJzdWIiOiIxMjk0Njc3ODQ5Njc3MDM4MjkiLCJjdHMiOiJPQVVUSDJfU1RBVEVMRVNTX0dSQU5UIiwiYXV0aF9sZXZlbCI6MCwiYXVkaXRUcmFja2luZ0lkIjoiMTlhMDFmOWMtNDY3Yi00ZWQ5LWFhZWUtMTkxNjVjY2ExNTg2LTM5MTgzNDkzIiwiaXNzIjoiaHR0cHM6Ly9hY2Nlc3MuYXBpLmJiYy5jb20vYmJjaWR2NS9vYXV0aDIiLCJ0b2tlbk5hbWUiOiJhY2Nlc3NfdG9rZW4iLCJ0b2tlbl90eXBlIjoiQmVhcmVyIiwiYXV0aEdyYW50SWQiOiJZV1QzY3h1SnVLR1FRZmVrNl9IY2R1V1pkNzAiLCJhdWQiOiJBY2NvdW50IiwibmJmIjoxNTg2MTY0NTU1LCJncmFudF90eXBlIjoicmVmcmVzaF90b2tlbiIsInNjb3BlIjpbImV4cGxpY2l0IiwidWlkIiwiaW1wbGljaXQiLCJwaWkiLCJjb3JlIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTU3MDcxNDM4MiwicmVhbG0iOiIvIiwiZXhwIjoxNTg2MTcxNzU1LCJpYXQiOjE1ODYxNjQ1NTUsImV4cGlyZXNfaW4iOjcyMDAsImp0aSI6InZoMXIxcTN5UmZ2RHR1Q1lrTkhlTzFablljOCJ9.s2_cjPjRtHIprcEQ9CrY913Sa_fFgMws9W7gvbHBEmf6IHJeVuE4v_z8Vj6y-vBjrxmp34YEwND8YzMR5f2Hyw; ckns_idtkn=eyJ0eXAiOiJKV1QiLCJraWQiOiJIa2d0WDBJd3RDOStSVGQvOWdYdFN0bk9VaU09IiwiYWxnIjoiUlMyNTYifQ.eyJhdF9oYXNoIjoiNjNjLWRzZ3F4U1FmSC1hNzA0OGlVZyIsInN1YiI6IjEyOTQ2Nzc4NDk2NzcwMzgyOSIsInVzZXJBdHRyaWJ1dGVzIjp7ImFiIjoibzE4IiwiZG4iOiJyb3Zpbmdyb3ZlciIsInBhIjoiQ004IiwiZXAiOnRydWUsImV2Ijp0cnVlLCJwbCI6ZmFsc2UsInBzIjoieEVXd1NsVF9Mcms0NU4yb2daelhyRFdJUUJpYTB5YUxxLTFjNHdXbHhTdyIsInN5IjoiRGVuMW53ZjU5VnhXRTRJanJWWlNvWDR3WU9hSG1rS2ZOQVY2YUN3cEUwZyIsImNsIjpmYWxzZX0sImF1ZGl0VHJhY2tpbmdJZCI6IjE5YTAxZjljLTQ2N2ItNGVkOS1hYWVlLTE5MTY1Y2NhMTU4Ni0zOTE4MzQ5NyIsImlzcyI6Imh0dHBzOi8vYWNjZXNzLmFwaS5iYmMuY29tL2JiY2lkdjUvb2F1dGgyIiwidG9rZW5OYW1lIjoiaWRfdG9rZW4iLCJhdWQiOiJBY2NvdW50IiwiYWNyIjoiMCIsImF6cCI6IkFjY291bnQiLCJhdXRoX3RpbWUiOjE1NzA3MTQzODIsInJlYWxtIjoiLyIsImV4cCI6MTU4NjE2ODE1NSwidG9rZW5UeXBlIjoiSldUVG9rZW4iLCJpYXQiOjE1ODYxNjQ1NTV9.ek1S4OJVXjlbAJFY6ux90JlZpQtHFeBpDlfjF22GzDH0HBlf3heNapUo8BhFIJXxGALt1U8WOmWIh_-Zd59KzFZdiyctP-LyfnVLefqo5CnIMdl6VydSM6JLCweZPQyaLDeRxNpDJDc3mzLLz4A5XNgzozuhGiuYySXCbF2Sta2YiY4Ng0_4UV-Li2fUTeYNDQC-dJvi5YsPC4aTPAWDO-VrHwVqaiyxx0xpMhB2O9ZPeTsJZq2ZXY3owvmpsVkFkhtEuNMFHn1SiusLxC8cdAzOwt2Ly256SCkQrnjdgJPkwlFLpgPP-QnKpx-HreYqUlX_CEAGkZpb7ZGSq_lItQ
    Upgrade-Insecure-Requests: 1
    DNT: 1
    If-None-Match: W/"402f7-0Hc3CLUUujBhc3udatbw53n67J4"
    """
    expected = {
        "Host": "www.bbc.co.uk",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cookie": "ckns_explicit=1; ckns_sa_labels_persist={}; ckns_privacy=july2019; ckns_id=eyJkbiI6InJvdmluZ3JvdmVyIiwiYWIiOiJvMTgiLCJwYSI6IkNNOCIsImVwIjp0cnVlLCJldiI6dHJ1ZSwicGwiOmZhbHNlLCJwcyI6InhFV3dTbFRfTHJrNDVOMm9nWnpYckRXSVFCaWEweWFMcS0xYzR3V2x4U3ciLCJjbCI6ZmFsc2UsInNlcy1leHAiOjE1NzA3MTUyODIwMDAsImp3dC1leHAiOjE2MzM3ODYzODIwMDAsInJ0a24tZXhwIjoxNjMzNzg2MzgyMDAwLCJ0a24tZXhwIjoxNTg2MTY4MTU1MDAwfQ; ckns_stateless=1; ckns_sylphid=Den1nwf59VxWE4IjrVZSoX4wYOaHmkKfNAV6aCwpE0g; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22b79fb0f0-9d9e-4442-b1e4-248a9e2aa82a%22%2C%22options%22%3A%7B%22end%22%3A%222020-12-06T20%3A34%3A03.465Z%22%2C%22path%22%3A%22%2F%22%7D%7D; ckns_policy=000; ckns_policy_exp=1611081053599; ckns_pgAgeConfirm=true; ckns_bbcTvVod=true; ckns_mvt=d482285d-5a61-4a1e-bee1-84046473edac; ckns_orb_fig_cache={%22ad%22:0%2C%22ap%22:0%2C%22ck%22:1%2C%22eu%22:1%2C%22uk%22:1}; ecos.dt=1586133182864; ckns_nonce=_6-EAPVmOLMjF7WutnoHZt6u; ckns_atkn=eyJ0eXAiOiJKV1QiLCJ6aXAiOiJOT05FIiwia2lkIjoiRWdVVSs4TmhhQVlLYzZ5bG9DQnJuS1BUY2U4PSIsImFsZyI6IkVTMjU2In0.eyJzdWIiOiIxMjk0Njc3ODQ5Njc3MDM4MjkiLCJjdHMiOiJPQVVUSDJfU1RBVEVMRVNTX0dSQU5UIiwiYXV0aF9sZXZlbCI6MCwiYXVkaXRUcmFja2luZ0lkIjoiMTlhMDFmOWMtNDY3Yi00ZWQ5LWFhZWUtMTkxNjVjY2ExNTg2LTM5MTgzNDkzIiwiaXNzIjoiaHR0cHM6Ly9hY2Nlc3MuYXBpLmJiYy5jb20vYmJjaWR2NS9vYXV0aDIiLCJ0b2tlbk5hbWUiOiJhY2Nlc3NfdG9rZW4iLCJ0b2tlbl90eXBlIjoiQmVhcmVyIiwiYXV0aEdyYW50SWQiOiJZV1QzY3h1SnVLR1FRZmVrNl9IY2R1V1pkNzAiLCJhdWQiOiJBY2NvdW50IiwibmJmIjoxNTg2MTY0NTU1LCJncmFudF90eXBlIjoicmVmcmVzaF90b2tlbiIsInNjb3BlIjpbImV4cGxpY2l0IiwidWlkIiwiaW1wbGljaXQiLCJwaWkiLCJjb3JlIiwib3BlbmlkIl0sImF1dGhfdGltZSI6MTU3MDcxNDM4MiwicmVhbG0iOiIvIiwiZXhwIjoxNTg2MTcxNzU1LCJpYXQiOjE1ODYxNjQ1NTUsImV4cGlyZXNfaW4iOjcyMDAsImp0aSI6InZoMXIxcTN5UmZ2RHR1Q1lrTkhlTzFablljOCJ9.s2_cjPjRtHIprcEQ9CrY913Sa_fFgMws9W7gvbHBEmf6IHJeVuE4v_z8Vj6y-vBjrxmp34YEwND8YzMR5f2Hyw; ckns_idtkn=eyJ0eXAiOiJKV1QiLCJraWQiOiJIa2d0WDBJd3RDOStSVGQvOWdYdFN0bk9VaU09IiwiYWxnIjoiUlMyNTYifQ.eyJhdF9oYXNoIjoiNjNjLWRzZ3F4U1FmSC1hNzA0OGlVZyIsInN1YiI6IjEyOTQ2Nzc4NDk2NzcwMzgyOSIsInVzZXJBdHRyaWJ1dGVzIjp7ImFiIjoibzE4IiwiZG4iOiJyb3Zpbmdyb3ZlciIsInBhIjoiQ004IiwiZXAiOnRydWUsImV2Ijp0cnVlLCJwbCI6ZmFsc2UsInBzIjoieEVXd1NsVF9Mcms0NU4yb2daelhyRFdJUUJpYTB5YUxxLTFjNHdXbHhTdyIsInN5IjoiRGVuMW53ZjU5VnhXRTRJanJWWlNvWDR3WU9hSG1rS2ZOQVY2YUN3cEUwZyIsImNsIjpmYWxzZX0sImF1ZGl0VHJhY2tpbmdJZCI6IjE5YTAxZjljLTQ2N2ItNGVkOS1hYWVlLTE5MTY1Y2NhMTU4Ni0zOTE4MzQ5NyIsImlzcyI6Imh0dHBzOi8vYWNjZXNzLmFwaS5iYmMuY29tL2JiY2lkdjUvb2F1dGgyIiwidG9rZW5OYW1lIjoiaWRfdG9rZW4iLCJhdWQiOiJBY2NvdW50IiwiYWNyIjoiMCIsImF6cCI6IkFjY291bnQiLCJhdXRoX3RpbWUiOjE1NzA3MTQzODIsInJlYWxtIjoiLyIsImV4cCI6MTU4NjE2ODE1NSwidG9rZW5UeXBlIjoiSldUVG9rZW4iLCJpYXQiOjE1ODYxNjQ1NTV9.ek1S4OJVXjlbAJFY6ux90JlZpQtHFeBpDlfjF22GzDH0HBlf3heNapUo8BhFIJXxGALt1U8WOmWIh_-Zd59KzFZdiyctP-LyfnVLefqo5CnIMdl6VydSM6JLCweZPQyaLDeRxNpDJDc3mzLLz4A5XNgzozuhGiuYySXCbF2Sta2YiY4Ng0_4UV-Li2fUTeYNDQC-dJvi5YsPC4aTPAWDO-VrHwVqaiyxx0xpMhB2O9ZPeTsJZq2ZXY3owvmpsVkFkhtEuNMFHn1SiusLxC8cdAzOwt2Ly256SCkQrnjdgJPkwlFLpgPP-QnKpx-HreYqUlX_CEAGkZpb7ZGSq_lItQ",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "If-None-Match": 'W/"402f7-0Hc3CLUUujBhc3udatbw53n67J4"',
    }
    assert utils.format_header_string(headers) == expected


def test_session():
    s = utils.get_requests_session()
    with pytest.raises(r.exceptions.RequestException) as e:
        s.get("http://bbc.co.uk/made_up_page")
    assert "404" in str(e.value)
