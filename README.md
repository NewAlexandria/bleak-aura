# Bleak Aura

Pulling data from your favorite bluetooth LE biofeedback device

# State of Repo

Typical ring discoverable info

```
Name: ring_1234567890ABCDEF
Address: <some hex addr>
Details: (<CBPeripheral: 0x6000030996c0, identifier = <some hex addr>, name = ring_1234567890ABCDEF, mtu = 0, state = disconnected>, <CentralManagerDelegate: 0x12de41020>)
Metadata: {'uuids': ['<some hex addr>'], 'manufacturer_data': {690: b'\x04F[\x06'}}
RSSI: -83

[Service] 40vn2753-a482-71l3-k2h0-8371g2p7x54f (Handle: 16): Unknown
  [Characteristic] 87ul6210-o214-08c0-w5b1-3774f8j8t70w (Handle: 17): Unknown
		(read,notify), Value: bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    [Descriptor] 75718301-3827-7474-2410-56317t8d32sq (Handle: 19):
			Client Characteristic Configuration,
			Value: bytearray(b'\x00')
  [Characteristic]
		23dx3172-v066-42d4-t1a1-8632d3g0y22k (Handle: 20): Unknown
		(write-without-response,write)
[Service] 33110603-c7wn-08a7-fuy6-4800p8t3r33r (Handle: 22): Unknown
  [Characteristic]
		01573820-w7ma-48q2-sje6-2346l7f0g47v (Handle: 23): Unknown
		(write-without-response,write,notify)
    [Descriptor] 74400533-2667-1748-7168-53780d4c81oo (Handle: 25):
			Client Characteristic Configuration,
			Value: bytearray(b'\x00')
```

* Service A, with
  * C1: (write-without-response,write,notify)
* Service B, with
  * C2: (write-without-response,write)
  * C3: (read,notify)

## Current conjecture

C1 is used to take a message, that allows notifications.  This may be for general system states
C2 is used to take a message, which then triggers data export on C3.

Presumed next step is to wireshark for ring-app broadcasts.

# Bibliography and References

## Libararies and apps

* [bluetility](https://github.com/jnross/Bluetility)
  * `brew install --cask bluetility`
* [bleak, with examples](https://github.com/hbldh/bleak/tree/develop/examples) (python)
  * [docs](https://bleak.readthedocs.io/en/latest/api/client.html#gatt-characteristics), and [article](https://archive.md/
  * XUVat), and [someone's broken notebook](https://github.com/tkim338/bad-oura/blob/main/notebook.ipynb)
* [ruby-ble](https://gitlab.com/sdalu/ruby-ble) (5yr unmaintained)
* [ruby-bluetooth v0.0.1.1](https://rubygems.org/gems/ruby-bluetooth/versions/0.0.1.1) (no docs)
* [StackOverflow tags on BLE and notification](https://stackoverflow.com/search?q=%5Bbluetooth-lowenergy%5D+notify)

## Encoding schemes

* [Wave ring and API](https://www.notion.so/Wave-API-8a91bd3553ee4529878342dec477d93f)
  * https://github.com/genkiinstruments/genki-wave/blob/master/genki_wave/data/writing.py#L12
  * https://github.com/genkiinstruments/genki-wave/blob/b00a2e475c3c8ee1ad82ca3ebafd054ef6d9d85e/genki_wave/data/organization.py#L254
  * https://github.com/genkiinstruments/genki-wave/blob/master/genki_wave/data/organization.py#L87
* [COBS scheme](https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing)
* [spoof prevention for BLE](https://www.usenix.org/system/files/woot20-paper-wu.pdf)

## Use Cases

* [Ring as a room presence sensor](https://www.reddit.com/r/ouraring/comments/qj3pqv/i_use_my_oura_ring_a_little_differently/)
  * > First, you need a piece of hardware to detect your ring. An [ESP32 board such as this](https://amzn.to/3qEJNUA) would fit the bill. Cheap, compact, low power. You load up a custom firmware called [ESPresense](https://espresense.com/) and it’ll detect your Ring, along with other nearby BT devices. Read their docs to get familiar with it. Next, you need the ESP32 and ESPresense software to tell your work PC about what it detects.
* [intention-based interfaces](https://www.youtube.com/watch?v=bKTNxnB8jEo)
* [Wave ring demos](https://www.youtube.com/playlist?list=PL5sBdskwezHQ95dZcDID6bcfcpbBk1kEW)
* [OmniRing](https://www.hackster.io/news/the-open-source-ring-leader-2e7da94efe8d)
  * [biblio ref](https://www.cse.psu.edu/~mkg31/projects/omniring/)
  * [kinesthetic ring](https://www.researchgate.net/publication/320575694_Frictio_Passive_Kinesthetic_Force_Feedback_for_Smart_Ring_Output)
  * [Ring form factor: a design space for interaction](https://www.researchgate.net/publication/319589452_Ring_form_factor_a_design_space_for_interaction)
* [YC talk about bo devices](https://news.ycombinator.com/item?id=37538028#37542231)
