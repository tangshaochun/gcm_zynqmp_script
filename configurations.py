board = 'v4a'

# https://www.silabs.com/documents/public/reference-manuals/Si5345-44-42-D-RM.pdf
Si5345 = {
  "preamble": [0x0B,0x24,0xC0,    0x0B,0x25,0x00,  0x05,0x40,0x01],
  "soft reset": [0x00,0x1C,0x01],
  "postamble": [0x05,0x14,0x01,  0x00,0x1C,0x01, 0x05,0x40,0x00,  0x0B,0x24,0xC3,  0x0B,0x25,0x02]
}

frequencies = {
  "MixMHz": [
    0x00,0x0B,0x68,    0x00,0x16,0x02,    0x00,0x17,0x1C,    0x00,0x18,0x00,
    0x00,0x19,0xDD,    0x00,0x1A,0xDF,    0x00,0x2B,0x02,    0x00,0x2C,0x0F,
    0x00,0x2D,0x55,    0x00,0x2E,0x3B,    0x00,0x2F,0x00,    0x00,0x30,0x3B,
    0x00,0x31,0x00,    0x00,0x32,0x3B,    0x00,0x33,0x00,    0x00,0x34,0x3B,
    0x00,0x35,0x00,    0x00,0x36,0x3B,    0x00,0x37,0x00,    0x00,0x38,0x3B,
    0x00,0x39,0x00,    0x00,0x3A,0x3B,    0x00,0x3B,0x00,    0x00,0x3C,0x3B,
    0x00,0x3D,0x00,    0x00,0x3F,0xFF,    0x00,0x40,0x04,    0x00,0x41,0x0C,
    0x00,0x42,0x0C,    0x00,0x43,0x0C,    0x00,0x44,0x0C,    0x00,0x45,0x0C,
    0x00,0x46,0x32,    0x00,0x47,0x32,    0x00,0x48,0x32,    0x00,0x49,0x32,
    0x00,0x4A,0x32,    0x00,0x4B,0x32,    0x00,0x4C,0x32,    0x00,0x4D,0x32,
    0x00,0x4E,0x55,    0x00,0x4F,0x55,    0x00,0x51,0x03,    0x00,0x52,0x03,
    0x00,0x53,0x03,    0x00,0x54,0x03,    0x00,0x55,0x03,    0x00,0x56,0x03,
    0x00,0x57,0x03,    0x00,0x58,0x03,    0x00,0x59,0xFF,    0x00,0x5A,0x31,
    0x00,0x5B,0xC1,    0x00,0x5C,0xD5,    0x00,0x5D,0x00,    0x00,0x5E,0x31,
    0x00,0x5F,0xC1,    0x00,0x60,0xD5,    0x00,0x61,0x00,    0x00,0x62,0x31,
    0x00,0x63,0xC1,    0x00,0x64,0xD5,    0x00,0x65,0x00,    0x00,0x66,0x31,
    0x00,0x67,0xC1,    0x00,0x68,0xD5,    0x00,0x69,0x00,    0x00,0x92,0x00,
    0x00,0x93,0x00,    0x00,0x95,0x00,    0x00,0x96,0x00,    0x00,0x98,0x00,
    0x00,0x9A,0x02,    0x00,0x9B,0x30,    0x00,0x9D,0x00,    0x00,0x9E,0x20,
    0x00,0xA0,0x00,    0x00,0xA2,0x02,    0x00,0xA8,0xCE,    0x00,0xA9,0x19,
    0x00,0xAA,0x09,    0x00,0xAB,0x00,    0x00,0xAC,0x00,

    0x01,0x02,0x01,    0x01,0x08,0x06,    0x01,0x09,0x09,    0x01,0x0A,0x3D,
    0x01,0x0B,0x02,    0x01,0x0D,0x06,    0x01,0x0E,0x09,    0x01,0x0F,0x3D,
    0x01,0x10,0x00,    0x01,0x12,0x06,    0x01,0x13,0x09,    0x01,0x14,0x3D,
    0x01,0x15,0x00,    0x01,0x17,0x06,    0x01,0x18,0x09,    0x01,0x19,0x3D,
    0x01,0x1A,0x01,    0x01,0x1C,0x06,    0x01,0x1D,0x09,    0x01,0x1E,0x3D,
    0x01,0x1F,0x00,    0x01,0x21,0x06,    0x01,0x22,0x09,    0x01,0x23,0x3D,
    0x01,0x24,0x00,    0x01,0x26,0x06,    0x01,0x27,0x09,    0x01,0x28,0x3D,
    0x01,0x29,0x02,    0x01,0x2B,0x06,    0x01,0x2C,0x09,    0x01,0x2D,0x3D,
    0x01,0x2E,0x02,    0x01,0x30,0x06,    0x01,0x31,0x09,    0x01,0x32,0x3D,
    0x01,0x33,0x02,    0x01,0x3A,0x02,    0x01,0x3B,0x09,    0x01,0x3C,0x3D,
    0x01,0x3D,0x00,    0x01,0x3F,0x00,    0x01,0x40,0x08,    0x01,0x41,0x40,
    0x01,0x42,0xFF,

    0x02,0x02,0x00,    0x02,0x03,0x00,    0x02,0x04,0x00,    0x02,0x05,0x00,
    0x02,0x06,0x00,    0x02,0x08,0x15,    0x02,0x09,0x00,    0x02,0x0A,0x00,
    0x02,0x0B,0x00,    0x02,0x0C,0x00,    0x02,0x0D,0x00,    0x02,0x0E,0x01,
    0x02,0x0F,0x00,    0x02,0x10,0x00,    0x02,0x11,0x00,    0x02,0x12,0x15,
    0x02,0x13,0x00,    0x02,0x14,0x00,    0x02,0x15,0x00,    0x02,0x16,0x00,
    0x02,0x17,0x00,    0x02,0x18,0x01,    0x02,0x19,0x00,    0x02,0x1A,0x00,
    0x02,0x1B,0x00,    0x02,0x1C,0x15,    0x02,0x1D,0x00,    0x02,0x1E,0x00,
    0x02,0x1F,0x00,    0x02,0x20,0x00,    0x02,0x21,0x00,    0x02,0x22,0x01,
    0x02,0x23,0x00,    0x02,0x24,0x00,    0x02,0x25,0x00,    0x02,0x26,0x15,
    0x02,0x27,0x00,    0x02,0x28,0x00,    0x02,0x29,0x00,    0x02,0x2A,0x00,
    0x02,0x2B,0x00,    0x02,0x2C,0x01,    0x02,0x2D,0x00,    0x02,0x2E,0x00,
    0x02,0x2F,0x00,    0x02,0x31,0x01,    0x02,0x32,0x01,    0x02,0x33,0x01,
    0x02,0x34,0x01,    0x02,0x35,0x00,    0x02,0x36,0x00,    0x02,0x37,0x40,
    0x02,0x38,0xFA,    0x02,0x39,0x11,    0x02,0x3A,0x01,    0x02,0x3B,0x00,
    0x02,0x3C,0x00,    0x02,0x3D,0x00,    0x02,0x3E,0xF0,    0x02,0x4A,0x00,
    0x02,0x4B,0x00,    0x02,0x4C,0x00,    0x02,0x4D,0x00,    0x02,0x4E,0x00,
    0x02,0x4F,0x00,    0x02,0x50,0x00,    0x02,0x51,0x00,    0x02,0x52,0x00,
    0x02,0x53,0x00,    0x02,0x54,0x00,    0x02,0x55,0x00,    0x02,0x56,0x00,
    0x02,0x57,0x00,    0x02,0x58,0x00,    0x02,0x59,0x00,    0x02,0x5A,0x00,
    0x02,0x5B,0x00,    0x02,0x5C,0x00,    0x02,0x5D,0x00,    0x02,0x5E,0x00,
    0x02,0x5F,0x00,    0x02,0x60,0x00,    0x02,0x61,0x00,    0x02,0x62,0x00,
    0x02,0x63,0x00,    0x02,0x64,0x00,    0x02,0x68,0x06,    0x02,0x69,0x00,
    0x02,0x6A,0x00,    0x02,0x6B,0x00,    0x02,0x6C,0x00,    0x02,0x6D,0x00,
    0x02,0x6E,0x00,    0x02,0x6F,0x00,    0x02,0x70,0x00,    0x02,0x71,0x00,
    0x02,0x72,0x00,

    0x03,0x02,0x00,    0x03,0x03,0x00,    0x03,0x04,0x00,    0x03,0x05,0x80,
    0x03,0x06,0x0C,    0x03,0x07,0x00,    0x03,0x08,0x00,    0x03,0x09,0x00,
    0x03,0x0A,0x00,    0x03,0x0B,0x80,    0x03,0x0D,0x00,    0x03,0x0E,0x00,
    0x03,0x0F,0x00,    0x03,0x10,0xF0,    0x03,0x11,0x0A,    0x03,0x12,0x00,
    0x03,0x13,0x00,    0x03,0x14,0x00,    0x03,0x15,0x00,    0x03,0x16,0x80,
    0x03,0x18,0x00,    0x03,0x19,0x00,    0x03,0x1A,0x00,    0x03,0x1B,0xE0,
    0x03,0x1C,0x15,    0x03,0x1D,0x00,    0x03,0x1E,0x00,    0x03,0x1F,0x00,
    0x03,0x20,0x00,    0x03,0x21,0xC0,    0x03,0x23,0x00,    0x03,0x24,0x00,
    0x03,0x25,0x00,    0x03,0x26,0x00,    0x03,0x27,0x00,    0x03,0x28,0x00,
    0x03,0x29,0x00,    0x03,0x2A,0x00,    0x03,0x2B,0x00,    0x03,0x2C,0x00,
    0x03,0x2E,0x00,    0x03,0x2F,0x00,    0x03,0x30,0x00,    0x03,0x31,0x00,
    0x03,0x32,0x00,    0x03,0x33,0x00,    0x03,0x34,0x00,    0x03,0x35,0x00,
    0x03,0x36,0x00,    0x03,0x37,0x00,    0x03,0x39,0x1F,    0x03,0x3B,0x00,
    0x03,0x3C,0x00,    0x03,0x3D,0x00,    0x03,0x3E,0x00,    0x03,0x3F,0x00,
    0x03,0x40,0x00,    0x03,0x41,0x00,    0x03,0x42,0x00,    0x03,0x43,0x00,
    0x03,0x44,0x00,    0x03,0x45,0x00,    0x03,0x46,0x00,    0x03,0x47,0x00,
    0x03,0x48,0x00,    0x03,0x49,0x00,    0x03,0x4A,0x00,    0x03,0x4B,0x00,
    0x03,0x4C,0x00,    0x03,0x4D,0x00,    0x03,0x4E,0x00,    0x03,0x4F,0x00,
    0x03,0x50,0x00,    0x03,0x51,0x00,    0x03,0x52,0x00,    0x03,0x53,0x00,
    0x03,0x54,0x00,    0x03,0x55,0x00,    0x03,0x56,0x00,    0x03,0x57,0x00,
    0x03,0x58,0x00,    0x03,0x59,0x00,    0x03,0x5A,0x00,    0x03,0x5B,0x00,
    0x03,0x5C,0x00,    0x03,0x5D,0x00,    0x03,0x5E,0x00,    0x03,0x5F,0x00,
    0x03,0x60,0x00,    0x03,0x61,0x00,    0x03,0x62,0x00,

    0x04,0x87,0x01,

    0x05,0x02,0x01,    0x05,0x08,0x14,    0x05,0x09,0x23,    0x05,0x0A,0x0C,
    0x05,0x0B,0x0B,    0x05,0x0C,0x03,    0x05,0x0D,0x3F,    0x05,0x0E,0x17,
    0x05,0x0F,0x2B,    0x05,0x10,0x09,    0x05,0x11,0x08,    0x05,0x12,0x03,
    0x05,0x13,0x3F,    0x05,0x15,0x00,    0x05,0x16,0x00,    0x05,0x17,0x00,
    0x05,0x18,0x00,    0x05,0x19,0xDF,    0x05,0x1A,0x02,    0x05,0x1B,0x00,
    0x05,0x1C,0x00,    0x05,0x1D,0x00,    0x05,0x1E,0x00,    0x05,0x1F,0x80,
    0x05,0x21,0x21,    0x05,0x2A,0x01,    0x05,0x2B,0x01,    0x05,0x2C,0x0F,
    0x05,0x2D,0x03,    0x05,0x2E,0x19,    0x05,0x2F,0x19,    0x05,0x31,0x00,
    0x05,0x32,0x6A,    0x05,0x33,0x03,    0x05,0x34,0x00,    0x05,0x36,0x08,
    0x05,0x37,0x00,    0x05,0x38,0x00,    0x05,0x39,0x00,

    0x09,0x0E,0x02,    0x09,0x43,0x01,    0x09,0x49,0x0F,    0x09,0x4A,0x0F,

    0x0A,0x02,0x00,    0x0A,0x03,0x07,    0x0A,0x04,0x01,    0x0A,0x05,0x07,

    0x0B,0x44,0x2F,    0x0B,0x46,0x00,    0x0B,0x47,0x00,    0x0B,0x48,0x00,
    0x0B,0x4A,0x18,

    0x05,0x14,0x01
  ],
  "240MHz": [
    0x00,0x0B,0x68,    0x00,0x16,0x02,    0x00,0x17,0x1C,    0x00,0x18,0x44,
    0x00,0x19,0xDD,    0x00,0x1A,0xDF,    0x00,0x2B,0x02,    0x00,0x2C,0x0B,
    0x00,0x2D,0x45,    0x00,0x2E,0x46,    0x00,0x2F,0x00,    0x00,0x30,0x46,
    0x00,0x31,0x00,    0x00,0x32,0x00,    0x00,0x33,0x00,    0x00,0x34,0x46,
    0x00,0x35,0x00,    0x00,0x36,0x46,    0x00,0x37,0x00,    0x00,0x38,0x46,
    0x00,0x39,0x00,    0x00,0x3A,0x00,    0x00,0x3B,0x00,    0x00,0x3C,0x46,
    0x00,0x3D,0x00,    0x00,0x3F,0xBB,    0x00,0x40,0x04,    0x00,0x41,0x0C,
    0x00,0x42,0x0C,    0x00,0x43,0x00,    0x00,0x44,0x0C,    0x00,0x45,0x0C,
    0x00,0x46,0x32,    0x00,0x47,0x32,    0x00,0x48,0x00,    0x00,0x49,0x32,
    0x00,0x4A,0x32,    0x00,0x4B,0x32,    0x00,0x4C,0x00,    0x00,0x4D,0x32,
    0x00,0x4E,0x55,    0x00,0x4F,0x50,    0x00,0x51,0x03,    0x00,0x52,0x03,
    0x00,0x53,0x00,    0x00,0x54,0x03,    0x00,0x55,0x03,    0x00,0x56,0x03,
    0x00,0x57,0x00,    0x00,0x58,0x03,    0x00,0x59,0xCF,    0x00,0x5A,0x31,
    0x00,0x5B,0xC1,    0x00,0x5C,0xD5,    0x00,0x5D,0x00,    0x00,0x5E,0x31,
    0x00,0x5F,0xC1,    0x00,0x60,0xD5,    0x00,0x61,0x00,    0x00,0x62,0x00,
    0x00,0x63,0x00,    0x00,0x64,0x00,    0x00,0x65,0x00,    0x00,0x66,0x31,
    0x00,0x67,0xC1,    0x00,0x68,0xD5,    0x00,0x69,0x00,    0x00,0x92,0x00,
    0x00,0x93,0x00,    0x00,0x95,0x00,    0x00,0x96,0x00,    0x00,0x98,0x00,
    0x00,0x9A,0x02,    0x00,0x9B,0x40,    0x00,0x9D,0x00,    0x00,0x9E,0x20,
    0x00,0xA0,0x00,    0x00,0xA2,0x02,    0x00,0xA8,0xD6,    0x00,0xA9,0x01,
    0x00,0xAA,0x09,    0x00,0xAB,0x00,    0x00,0xAC,0x00,

    0x01,0x02,0x01,    0x01,0x08,0x06,    0x01,0x09,0x09,    0x01,0x0A,0x3D,
    0x01,0x0B,0x00,    0x01,0x0D,0x06,    0x01,0x0E,0x09,    0x01,0x0F,0x3D,
    0x01,0x10,0x00,    0x01,0x12,0x06,    0x01,0x13,0x09,    0x01,0x14,0x3D,
    0x01,0x15,0x00,    0x01,0x17,0x06,    0x01,0x18,0x09,    0x01,0x19,0x3D,
    0x01,0x1A,0x00,    0x01,0x1C,0x06,    0x01,0x1D,0x09,    0x01,0x1E,0x3D,
    0x01,0x1F,0x00,    0x01,0x21,0x06,    0x01,0x22,0x09,    0x01,0x23,0x3D,
    0x01,0x24,0x00,    0x01,0x26,0x06,    0x01,0x27,0x09,    0x01,0x28,0x3D,
    0x01,0x29,0x00,    0x01,0x2B,0x06,    0x01,0x2C,0x09,    0x01,0x2D,0x3D,
    0x01,0x2E,0x00,    0x01,0x30,0x06,    0x01,0x31,0x09,    0x01,0x32,0x3D,
    0x01,0x33,0x00,    0x01,0x3A,0x02,    0x01,0x3B,0x09,    0x01,0x3C,0x3D,
    0x01,0x3D,0x00,    0x01,0x3F,0x00,    0x01,0x40,0x08,    0x01,0x41,0x40,
    0x01,0x42,0xFF,

    0x02,0x02,0x00,    0x02,0x03,0x00,    0x02,0x04,0x00,    0x02,0x05,0x00,
    0x02,0x06,0x00,    0x02,0x08,0x19,    0x02,0x09,0x00,    0x02,0x0A,0x00,
    0x02,0x0B,0x00,    0x02,0x0C,0x00,    0x02,0x0D,0x00,    0x02,0x0E,0x01,
    0x02,0x0F,0x00,    0x02,0x10,0x00,    0x02,0x11,0x00,    0x02,0x12,0x19,
    0x02,0x13,0x00,    0x02,0x14,0x00,    0x02,0x15,0x00,    0x02,0x16,0x00,
    0x02,0x17,0x00,    0x02,0x18,0x01,    0x02,0x19,0x00,    0x02,0x1A,0x00,
    0x02,0x1B,0x00,    0x02,0x1C,0x00,    0x02,0x1D,0x00,    0x02,0x1E,0x00,
    0x02,0x1F,0x00,    0x02,0x20,0x00,    0x02,0x21,0x00,    0x02,0x22,0x00,
    0x02,0x23,0x00,    0x02,0x24,0x00,    0x02,0x25,0x00,    0x02,0x26,0x19,
    0x02,0x27,0x00,    0x02,0x28,0x00,    0x02,0x29,0x00,    0x02,0x2A,0x00,
    0x02,0x2B,0x00,    0x02,0x2C,0x01,    0x02,0x2D,0x00,    0x02,0x2E,0x00,
    0x02,0x2F,0x00,    0x02,0x31,0x01,    0x02,0x32,0x01,    0x02,0x33,0x01,
    0x02,0x34,0x01,    0x02,0x35,0x00,    0x02,0x36,0x00,    0x02,0x37,0x30,
    0x02,0x38,0xC3,    0x02,0x39,0x1B,    0x02,0x3A,0x01,    0x02,0x3B,0x00,
    0x02,0x3C,0x00,    0x02,0x3D,0x00,    0x02,0x3E,0xFA,    0x02,0x4A,0x00,
    0x02,0x4B,0x00,    0x02,0x4C,0x00,    0x02,0x4D,0x00,    0x02,0x4E,0x00,
    0x02,0x4F,0x00,    0x02,0x50,0x00,    0x02,0x51,0x00,    0x02,0x52,0x00,
    0x02,0x53,0x00,    0x02,0x54,0x00,    0x02,0x55,0x00,    0x02,0x56,0x00,
    0x02,0x57,0x00,    0x02,0x58,0x00,    0x02,0x59,0x00,    0x02,0x5A,0x00,
    0x02,0x5B,0x00,    0x02,0x5C,0x00,    0x02,0x5D,0x00,    0x02,0x5E,0x00,
    0x02,0x5F,0x00,    0x02,0x60,0x00,    0x02,0x61,0x00,    0x02,0x62,0x00,
    0x02,0x63,0x00,    0x02,0x64,0x00,    0x02,0x68,0x05,    0x02,0x69,0x00,
    0x02,0x6A,0x00,    0x02,0x6B,0x00,    0x02,0x6C,0x00,    0x02,0x6D,0x00,
    0x02,0x6E,0x00,    0x02,0x6F,0x00,    0x02,0x70,0x00,    0x02,0x71,0x00,
    0x02,0x72,0x00,

    0x03,0x02,0x00,    0x03,0x03,0x00,    0x03,0x04,0x00,    0x03,0x05,0x80,
    0x03,0x06,0x0E,    0x03,0x07,0x00,    0x03,0x08,0x00,    0x03,0x09,0x00,
    0x03,0x0A,0x00,    0x03,0x0B,0x80,    0x03,0x0D,0x00,    0x03,0x0E,0x00,
    0x03,0x0F,0x00,    0x03,0x10,0x00,    0x03,0x11,0x00,    0x03,0x12,0x00,
    0x03,0x13,0x00,    0x03,0x14,0x00,    0x03,0x15,0x00,    0x03,0x16,0x00,
    0x03,0x18,0x00,    0x03,0x19,0x00,    0x03,0x1A,0x00,    0x03,0x1B,0x00,
    0x03,0x1C,0x00,    0x03,0x1D,0x00,    0x03,0x1E,0x00,    0x03,0x1F,0x00,
    0x03,0x20,0x00,    0x03,0x21,0x00,    0x03,0x23,0x00,    0x03,0x24,0x00,
    0x03,0x25,0x00,    0x03,0x26,0x00,    0x03,0x27,0x00,    0x03,0x28,0x00,
    0x03,0x29,0x00,    0x03,0x2A,0x00,    0x03,0x2B,0x00,    0x03,0x2C,0x00,
    0x03,0x2E,0x00,    0x03,0x2F,0x00,    0x03,0x30,0x00,    0x03,0x31,0x00,
    0x03,0x32,0x00,    0x03,0x33,0x00,    0x03,0x34,0x00,    0x03,0x35,0x00,
    0x03,0x36,0x00,    0x03,0x37,0x00,    0x03,0x39,0x1F,    0x03,0x3B,0x00,
    0x03,0x3C,0x00,    0x03,0x3D,0x00,    0x03,0x3E,0x00,    0x03,0x3F,0x00,
    0x03,0x40,0x00,    0x03,0x41,0x00,    0x03,0x42,0x00,    0x03,0x43,0x00,
    0x03,0x44,0x00,    0x03,0x45,0x00,    0x03,0x46,0x00,    0x03,0x47,0x00,
    0x03,0x48,0x00,    0x03,0x49,0x00,    0x03,0x4A,0x00,    0x03,0x4B,0x00,
    0x03,0x4C,0x00,    0x03,0x4D,0x00,    0x03,0x4E,0x00,    0x03,0x4F,0x00,
    0x03,0x50,0x00,    0x03,0x51,0x00,    0x03,0x52,0x00,    0x03,0x53,0x00,
    0x03,0x54,0x00,    0x03,0x55,0x00,    0x03,0x56,0x00,    0x03,0x57,0x00,
    0x03,0x58,0x00,    0x03,0x59,0x00,    0x03,0x5A,0x00,    0x03,0x5B,0x00,
    0x03,0x5C,0x00,    0x03,0x5D,0x00,    0x03,0x5E,0x00,    0x03,0x5F,0x00,
    0x03,0x60,0x00,    0x03,0x61,0x00,    0x03,0x62,0x00,

    0x04,0x87,0x01,

    0x05,0x02,0x01,    0x05,0x08,0x14,    0x05,0x09,0x23,    0x05,0x0A,0x0D,
    0x05,0x0B,0x0C,    0x05,0x0C,0x03,    0x05,0x0D,0x3F,    0x05,0x0E,0x18,
    0x05,0x0F,0x2D,    0x05,0x10,0x09,    0x05,0x11,0x08,    0x05,0x12,0x03,
    0x05,0x13,0x3F,    0x05,0x15,0x00,    0x05,0x16,0x00,    0x05,0x17,0x00,
    0x05,0x18,0x00,    0x05,0x19,0x66,    0x05,0x1A,0x03,    0x05,0x1B,0x00,
    0x05,0x1C,0x00,    0x05,0x1D,0x00,    0x05,0x1E,0x00,    0x05,0x1F,0x80,
    0x05,0x21,0x21,    0x05,0x2A,0x01,    0x05,0x2B,0x01,    0x05,0x2C,0x0F,
    0x05,0x2D,0x03,    0x05,0x2E,0x19,    0x05,0x2F,0x19,    0x05,0x31,0x00,
    0x05,0x32,0x10,    0x05,0x33,0x04,    0x05,0x34,0x00,    0x05,0x36,0x0C,
    0x05,0x37,0x00,    0x05,0x38,0x00,    0x05,0x39,0x00,

    0x09,0x0E,0x02,    0x09,0x43,0x01,    0x09,0x49,0x0B,    0x09,0x4A,0x0B,

    0x0A,0x02,0x00,    0x0A,0x03,0x01,    0x0A,0x04,0x01,    0x0A,0x05,0x01,

    0x0B,0x44,0x2F,    0x0B,0x46,0x00,    0x0B,0x47,0x00,    0x0B,0x48,0x04,
    0x0B,0x4A,0x1E,

    0x05,0x14,0x01
  ],
  "280MHz": [
		0x00,0x0B,0x68,    0x00,0x16,0x02,    0x00,0x17,0x1C,    0x00,0x18,0x66,
		0x00,0x19,0xDD,    0x00,0x1A,0xDF,    0x00,0x2B,0x02,    0x00,0x2C,0x09,
		0x00,0x2D,0x41,    0x00,0x2E,0x3B,    0x00,0x2F,0x00,    0x00,0x30,0x00,
		0x00,0x31,0x00,    0x00,0x32,0x00,    0x00,0x33,0x00,    0x00,0x34,0x3B,
		0x00,0x35,0x00,    0x00,0x36,0x3B,    0x00,0x37,0x00,    0x00,0x38,0x00,
		0x00,0x39,0x00,    0x00,0x3A,0x00,    0x00,0x3B,0x00,    0x00,0x3C,0x3B,
		0x00,0x3D,0x00,    0x00,0x3F,0x99,    0x00,0x40,0x04,    0x00,0x41,0x0C,
		0x00,0x42,0x00,    0x00,0x43,0x00,    0x00,0x44,0x0C,    0x00,0x45,0x0C,
		0x00,0x46,0x32,    0x00,0x47,0x00,    0x00,0x48,0x00,    0x00,0x49,0x32,
		0x00,0x4A,0x32,    0x00,0x4B,0x00,    0x00,0x4C,0x00,    0x00,0x4D,0x32,
		0x00,0x4E,0x05,    0x00,0x4F,0x50,    0x00,0x51,0x03,    0x00,0x52,0x00,
		0x00,0x53,0x00,    0x00,0x54,0x03,    0x00,0x55,0x03,    0x00,0x56,0x00,
		0x00,0x57,0x00,    0x00,0x58,0x03,    0x00,0x59,0xC3,    0x00,0x5A,0x31,
		0x00,0x5B,0xC1,    0x00,0x5C,0xD5,    0x00,0x5D,0x00,    0x00,0x5E,0x00,
		0x00,0x5F,0x00,    0x00,0x60,0x00,    0x00,0x61,0x00,    0x00,0x62,0x00,
		0x00,0x63,0x00,    0x00,0x64,0x00,    0x00,0x65,0x00,    0x00,0x66,0x31,
		0x00,0x67,0xC1,    0x00,0x68,0xD5,    0x00,0x69,0x00,    0x00,0x92,0x00,
		0x00,0x93,0x00,    0x00,0x95,0x00,    0x00,0x96,0x00,    0x00,0x98,0x00,
		0x00,0x9A,0x02,    0x00,0x9B,0x30,    0x00,0x9D,0x00,    0x00,0x9E,0x20,
		0x00,0xA0,0x00,    0x00,0xA2,0x02,    0x00,0xA8,0xED,    0x00,0xA9,0x33,
		0x00,0xAA,0x12,    0x00,0xAB,0x00,    0x00,0xAC,0x00,

		0x01,0x02,0x01,    0x01,0x08,0x06,    0x01,0x09,0x09,    0x01,0x0A,0x3D,
		0x01,0x0B,0x00,    0x01,0x0D,0x06,    0x01,0x0E,0x09,    0x01,0x0F,0x3D,
		0x01,0x10,0x00,    0x01,0x12,0x06,    0x01,0x13,0x09,    0x01,0x14,0x3D,
		0x01,0x15,0x00,    0x01,0x17,0x06,    0x01,0x18,0x09,    0x01,0x19,0x3D,
		0x01,0x1A,0x00,    0x01,0x1C,0x06,    0x01,0x1D,0x09,    0x01,0x1E,0x3D,
		0x01,0x1F,0x00,    0x01,0x21,0x06,    0x01,0x22,0x09,    0x01,0x23,0x3D,
		0x01,0x24,0x00,    0x01,0x26,0x06,    0x01,0x27,0x09,    0x01,0x28,0x3D,
		0x01,0x29,0x00,    0x01,0x2B,0x06,    0x01,0x2C,0x09,    0x01,0x2D,0x3D,
		0x01,0x2E,0x00,    0x01,0x30,0x06,    0x01,0x31,0x09,    0x01,0x32,0x3D,
		0x01,0x33,0x00,    0x01,0x3A,0x02,    0x01,0x3B,0x09,    0x01,0x3C,0x3D,
		0x01,0x3D,0x00,    0x01,0x3F,0x00,    0x01,0x40,0x08,    0x01,0x41,0x40,
		0x01,0x42,0xFF,

		0x02,0x02,0x00,    0x02,0x03,0x00,    0x02,0x04,0x00,    0x02,0x05,0x00,
		0x02,0x06,0x00,    0x02,0x08,0x15,    0x02,0x09,0x00,    0x02,0x0A,0x00,
		0x02,0x0B,0x00,    0x02,0x0C,0x00,    0x02,0x0D,0x00,    0x02,0x0E,0x01,
		0x02,0x0F,0x00,    0x02,0x10,0x00,    0x02,0x11,0x00,    0x02,0x12,0x00,
		0x02,0x13,0x00,    0x02,0x14,0x00,    0x02,0x15,0x00,    0x02,0x16,0x00,
		0x02,0x17,0x00,    0x02,0x18,0x00,    0x02,0x19,0x00,    0x02,0x1A,0x00,
		0x02,0x1B,0x00,    0x02,0x1C,0x00,    0x02,0x1D,0x00,    0x02,0x1E,0x00,
		0x02,0x1F,0x00,    0x02,0x20,0x00,    0x02,0x21,0x00,    0x02,0x22,0x00,
		0x02,0x23,0x00,    0x02,0x24,0x00,    0x02,0x25,0x00,    0x02,0x26,0x15,
		0x02,0x27,0x00,    0x02,0x28,0x00,    0x02,0x29,0x00,    0x02,0x2A,0x00,
		0x02,0x2B,0x00,    0x02,0x2C,0x01,    0x02,0x2D,0x00,    0x02,0x2E,0x00,
		0x02,0x2F,0x00,    0x02,0x31,0x01,    0x02,0x32,0x01,    0x02,0x33,0x01,
		0x02,0x34,0x01,    0x02,0x35,0x00,    0x02,0x36,0x00,    0x02,0x37,0x40,
		0x02,0x38,0xFA,    0x02,0x39,0x11,    0x02,0x3A,0x01,    0x02,0x3B,0x00,
		0x02,0x3C,0x00,    0x02,0x3D,0x00,    0x02,0x3E,0xF0,    0x02,0x4A,0x00,
		0x02,0x4B,0x00,    0x02,0x4C,0x00,    0x02,0x4D,0x00,    0x02,0x4E,0x00,
		0x02,0x4F,0x00,    0x02,0x50,0x00,    0x02,0x51,0x00,    0x02,0x52,0x00,
		0x02,0x53,0x00,    0x02,0x54,0x00,    0x02,0x55,0x00,    0x02,0x56,0x00,
		0x02,0x57,0x00,    0x02,0x58,0x00,    0x02,0x59,0x00,    0x02,0x5A,0x00,
		0x02,0x5B,0x00,    0x02,0x5C,0x00,    0x02,0x5D,0x00,    0x02,0x5E,0x00,
		0x02,0x5F,0x00,    0x02,0x60,0x00,    0x02,0x61,0x00,    0x02,0x62,0x00,
		0x02,0x63,0x00,    0x02,0x64,0x00,    0x02,0x68,0x06,    0x02,0x69,0x00,
		0x02,0x6A,0x00,    0x02,0x6B,0x00,    0x02,0x6C,0x00,    0x02,0x6D,0x00,
		0x02,0x6E,0x00,    0x02,0x6F,0x00,    0x02,0x70,0x00,    0x02,0x71,0x00,
		0x02,0x72,0x00,

		0x03,0x02,0x00,    0x03,0x03,0x00,    0x03,0x04,0x00,    0x03,0x05,0x80,
		0x03,0x06,0x0C,    0x03,0x07,0x00,    0x03,0x08,0x00,    0x03,0x09,0x00,
		0x03,0x0A,0x00,    0x03,0x0B,0x80,    0x03,0x0D,0x00,    0x03,0x0E,0x00,
		0x03,0x0F,0x00,    0x03,0x10,0x00,    0x03,0x11,0x00,    0x03,0x12,0x00,
		0x03,0x13,0x00,    0x03,0x14,0x00,    0x03,0x15,0x00,    0x03,0x16,0x00,
		0x03,0x18,0x00,    0x03,0x19,0x00,    0x03,0x1A,0x00,    0x03,0x1B,0x00,
		0x03,0x1C,0x00,    0x03,0x1D,0x00,    0x03,0x1E,0x00,    0x03,0x1F,0x00,
		0x03,0x20,0x00,    0x03,0x21,0x00,    0x03,0x23,0x00,    0x03,0x24,0x00,
		0x03,0x25,0x00,    0x03,0x26,0x00,    0x03,0x27,0x00,    0x03,0x28,0x00,
		0x03,0x29,0x00,    0x03,0x2A,0x00,    0x03,0x2B,0x00,    0x03,0x2C,0x00,
		0x03,0x2E,0x00,    0x03,0x2F,0x00,    0x03,0x30,0x00,    0x03,0x31,0x00,
		0x03,0x32,0x00,    0x03,0x33,0x00,    0x03,0x34,0x00,    0x03,0x35,0x00,
		0x03,0x36,0x00,    0x03,0x37,0x00,    0x03,0x39,0x1F,    0x03,0x3B,0x00,
		0x03,0x3C,0x00,    0x03,0x3D,0x00,    0x03,0x3E,0x00,    0x03,0x3F,0x00,
		0x03,0x40,0x00,    0x03,0x41,0x00,    0x03,0x42,0x00,    0x03,0x43,0x00,
		0x03,0x44,0x00,    0x03,0x45,0x00,    0x03,0x46,0x00,    0x03,0x47,0x00,
		0x03,0x48,0x00,    0x03,0x49,0x00,    0x03,0x4A,0x00,    0x03,0x4B,0x00,
		0x03,0x4C,0x00,    0x03,0x4D,0x00,    0x03,0x4E,0x00,    0x03,0x4F,0x00,
		0x03,0x50,0x00,    0x03,0x51,0x00,    0x03,0x52,0x00,    0x03,0x53,0x00,
		0x03,0x54,0x00,    0x03,0x55,0x00,    0x03,0x56,0x00,    0x03,0x57,0x00,
		0x03,0x58,0x00,    0x03,0x59,0x00,    0x03,0x5A,0x00,    0x03,0x5B,0x00,
		0x03,0x5C,0x00,    0x03,0x5D,0x00,    0x03,0x5E,0x00,    0x03,0x5F,0x00,
		0x03,0x60,0x00,    0x03,0x61,0x00,    0x03,0x62,0x00,

		0x04,0x87,0x01,

		0x05,0x02,0x01,    0x05,0x08,0x14,    0x05,0x09,0x22,    0x05,0x0A,0x0D,
		0x05,0x0B,0x0C,    0x05,0x0C,0x01,    0x05,0x0D,0x3F,    0x05,0x0E,0x18,
		0x05,0x0F,0x2C,    0x05,0x10,0x09,    0x05,0x11,0x08,    0x05,0x12,0x01,
		0x05,0x13,0x3F,    0x05,0x15,0x00,    0x05,0x16,0x00,    0x05,0x17,0x00,
		0x05,0x18,0x00,    0x05,0x19,0xDF,    0x05,0x1A,0x02,    0x05,0x1B,0x00,
		0x05,0x1C,0x00,    0x05,0x1D,0x00,    0x05,0x1E,0x00,    0x05,0x1F,0x80,
		0x05,0x21,0x21,    0x05,0x2A,0x01,    0x05,0x2B,0x01,    0x05,0x2C,0x0F,
		0x05,0x2D,0x03,    0x05,0x2E,0x19,    0x05,0x2F,0x19,    0x05,0x31,0x00,
		0x05,0x32,0x6A,    0x05,0x33,0x03,    0x05,0x34,0x00,    0x05,0x36,0x0C,
		0x05,0x37,0x00,    0x05,0x38,0x00,    0x05,0x39,0x00,

		0x09,0x0E,0x02,    0x09,0x43,0x01,    0x09,0x49,0x09,    0x09,0x4A,0x09,

		0x0A,0x02,0x00,    0x0A,0x03,0x01,    0x0A,0x04,0x01,    0x0A,0x05,0x01,

		0x0B,0x44,0x2F,    0x0B,0x46,0x00,    0x0B,0x47,0x00,    0x0B,0x48,0x06,
		0x0B,0x4A,0x1E,

		0x05,0x14,0x01
  ],
  "320MHz": [
    0x00,0x0B,0x68,    0x00,0x16,0x02,    0x00,0x17,0x1C,    0x00,0x18,0x00,
    0x00,0x19,0xDD,    0x00,0x1A,0xDF,    0x00,0x2B,0x02,    0x00,0x2C,0x0F,
    0x00,0x2D,0x55,    0x00,0x2E,0x47,    0x00,0x2F,0x00,    0x00,0x30,0x47,
    0x00,0x31,0x00,    0x00,0x32,0x47,    0x00,0x33,0x00,    0x00,0x34,0x47,
    0x00,0x35,0x00,    0x00,0x36,0x47,    0x00,0x37,0x00,    0x00,0x38,0x47,
    0x00,0x39,0x00,    0x00,0x3A,0x47,    0x00,0x3B,0x00,    0x00,0x3C,0x47,
    0x00,0x3D,0x00,    0x00,0x3F,0xFF,    0x00,0x40,0x04,    0x00,0x41,0x0C,
    0x00,0x42,0x0C,    0x00,0x43,0x0C,    0x00,0x44,0x0C,    0x00,0x45,0x0C,
    0x00,0x46,0x32,    0x00,0x47,0x32,    0x00,0x48,0x32,    0x00,0x49,0x32,
    0x00,0x4A,0x32,    0x00,0x4B,0x32,    0x00,0x4C,0x32,    0x00,0x4D,0x32,
    0x00,0x4E,0x55,    0x00,0x4F,0x55,    0x00,0x51,0x03,    0x00,0x52,0x03,
    0x00,0x53,0x03,    0x00,0x54,0x03,    0x00,0x55,0x03,    0x00,0x56,0x03,
    0x00,0x57,0x03,    0x00,0x58,0x03,    0x00,0x59,0xFF,    0x00,0x5A,0x31,
    0x00,0x5B,0xC1,    0x00,0x5C,0xD5,    0x00,0x5D,0x00,    0x00,0x5E,0x31,
    0x00,0x5F,0xC1,    0x00,0x60,0xD5,    0x00,0x61,0x00,    0x00,0x62,0x31,
    0x00,0x63,0xC1,    0x00,0x64,0xD5,    0x00,0x65,0x00,    0x00,0x66,0x31,
    0x00,0x67,0xC1,    0x00,0x68,0xD5,    0x00,0x69,0x00,    0x00,0x92,0x00,
    0x00,0x93,0x00,    0x00,0x95,0x00,    0x00,0x96,0x00,    0x00,0x98,0x00,
    0x00,0x9A,0x02,    0x00,0x9B,0x40,    0x00,0x9D,0x00,    0x00,0x9E,0x20,
    0x00,0xA0,0x00,    0x00,0xA2,0x02,    0x00,0xA8,0x0C,    0x00,0xA9,0x50,
    0x00,0xAA,0x09,    0x00,0xAB,0x00,    0x00,0xAC,0x00,

    0x01,0x02,0x01,    0x01,0x08,0x06,    0x01,0x09,0x09,    0x01,0x0A,0x3D,
    0x01,0x0B,0x00,    0x01,0x0D,0x06,    0x01,0x0E,0x09,    0x01,0x0F,0x3D,
    0x01,0x10,0x00,    0x01,0x12,0x06,    0x01,0x13,0x09,    0x01,0x14,0x3D,
    0x01,0x15,0x00,    0x01,0x17,0x06,    0x01,0x18,0x09,    0x01,0x19,0x3D,
    0x01,0x1A,0x00,    0x01,0x1C,0x06,    0x01,0x1D,0x09,    0x01,0x1E,0x3D,
    0x01,0x1F,0x00,    0x01,0x21,0x06,    0x01,0x22,0x09,    0x01,0x23,0x3D,
    0x01,0x24,0x00,    0x01,0x26,0x06,    0x01,0x27,0x09,    0x01,0x28,0x3D,
    0x01,0x29,0x00,    0x01,0x2B,0x06,    0x01,0x2C,0x09,    0x01,0x2D,0x3D,
    0x01,0x2E,0x00,    0x01,0x30,0x06,    0x01,0x31,0x09,    0x01,0x32,0x3D,
    0x01,0x33,0x00,    0x01,0x3A,0x02,    0x01,0x3B,0x09,    0x01,0x3C,0x3D,
    0x01,0x3D,0x00,    0x01,0x3F,0x00,    0x01,0x40,0x08,    0x01,0x41,0x40,
    0x01,0x42,0xFF,

    0x02,0x02,0x00,    0x02,0x03,0x00,    0x02,0x04,0x00,    0x02,0x05,0x00,
    0x02,0x06,0x00,    0x02,0x08,0x19,    0x02,0x09,0x00,    0x02,0x0A,0x00,
    0x02,0x0B,0x00,    0x02,0x0C,0x00,    0x02,0x0D,0x00,    0x02,0x0E,0x01,
    0x02,0x0F,0x00,    0x02,0x10,0x00,    0x02,0x11,0x00,    0x02,0x12,0x19,
    0x02,0x13,0x00,    0x02,0x14,0x00,    0x02,0x15,0x00,    0x02,0x16,0x00,
    0x02,0x17,0x00,    0x02,0x18,0x01,    0x02,0x19,0x00,    0x02,0x1A,0x00,
    0x02,0x1B,0x00,    0x02,0x1C,0x19,    0x02,0x1D,0x00,    0x02,0x1E,0x00,
    0x02,0x1F,0x00,    0x02,0x20,0x00,    0x02,0x21,0x00,    0x02,0x22,0x01,
    0x02,0x23,0x00,    0x02,0x24,0x00,    0x02,0x25,0x00,    0x02,0x26,0x19,
    0x02,0x27,0x00,    0x02,0x28,0x00,    0x02,0x29,0x00,    0x02,0x2A,0x00,
    0x02,0x2B,0x00,    0x02,0x2C,0x01,    0x02,0x2D,0x00,    0x02,0x2E,0x00,
    0x02,0x2F,0x00,    0x02,0x31,0x01,    0x02,0x32,0x01,    0x02,0x33,0x01,
    0x02,0x34,0x01,    0x02,0x35,0x00,    0x02,0x36,0x00,    0x02,0x37,0xA0,
    0x02,0x38,0x44,    0x02,0x39,0xD7,    0x02,0x3A,0x00,    0x02,0x3B,0x00,
    0x02,0x3C,0x00,    0x02,0x3D,0x80,    0x02,0x3E,0xBB,    0x02,0x4A,0x00,
    0x02,0x4B,0x00,    0x02,0x4C,0x00,    0x02,0x4D,0x00,    0x02,0x4E,0x00,
    0x02,0x4F,0x00,    0x02,0x50,0x00,    0x02,0x51,0x00,    0x02,0x52,0x00,
    0x02,0x53,0x00,    0x02,0x54,0x00,    0x02,0x55,0x00,    0x02,0x56,0x00,
    0x02,0x57,0x00,    0x02,0x58,0x00,    0x02,0x59,0x00,    0x02,0x5A,0x00,
    0x02,0x5B,0x00,    0x02,0x5C,0x00,    0x02,0x5D,0x00,    0x02,0x5E,0x00,
    0x02,0x5F,0x00,    0x02,0x60,0x00,    0x02,0x61,0x00,    0x02,0x62,0x00,
    0x02,0x63,0x00,    0x02,0x64,0x00,    0x02,0x68,0x07,    0x02,0x69,0x00,
    0x02,0x6A,0x00,    0x02,0x6B,0x00,    0x02,0x6C,0x00,    0x02,0x6D,0x00,
    0x02,0x6E,0x00,    0x02,0x6F,0x00,    0x02,0x70,0x00,    0x02,0x71,0x00,
    0x02,0x72,0x00,

    0x03,0x02,0x00,    0x03,0x03,0x00,    0x03,0x04,0x00,    0x03,0x05,0x00,
    0x03,0x06,0x0B,    0x03,0x07,0x00,    0x03,0x08,0x00,    0x03,0x09,0x00,
    0x03,0x0A,0x00,    0x03,0x0B,0x80,    0x03,0x0D,0x00,    0x03,0x0E,0x00,
    0x03,0x0F,0x00,    0x03,0x10,0x00,    0x03,0x11,0x00,    0x03,0x12,0x00,
    0x03,0x13,0x00,    0x03,0x14,0x00,    0x03,0x15,0x00,    0x03,0x16,0x00,
    0x03,0x18,0x00,    0x03,0x19,0x00,    0x03,0x1A,0x00,    0x03,0x1B,0x00,
    0x03,0x1C,0x00,    0x03,0x1D,0x00,    0x03,0x1E,0x00,    0x03,0x1F,0x00,
    0x03,0x20,0x00,    0x03,0x21,0x00,    0x03,0x23,0x00,    0x03,0x24,0x00,
    0x03,0x25,0x00,    0x03,0x26,0x00,    0x03,0x27,0x00,    0x03,0x28,0x00,
    0x03,0x29,0x00,    0x03,0x2A,0x00,    0x03,0x2B,0x00,    0x03,0x2C,0x00,
    0x03,0x2E,0x00,    0x03,0x2F,0x00,    0x03,0x30,0x00,    0x03,0x31,0x00,
    0x03,0x32,0x00,    0x03,0x33,0x00,    0x03,0x34,0x00,    0x03,0x35,0x00,
    0x03,0x36,0x00,    0x03,0x37,0x00,    0x03,0x39,0x1F,    0x03,0x3B,0x00,
    0x03,0x3C,0x00,    0x03,0x3D,0x00,    0x03,0x3E,0x00,    0x03,0x3F,0x00,
    0x03,0x40,0x00,    0x03,0x41,0x00,    0x03,0x42,0x00,    0x03,0x43,0x00,
    0x03,0x44,0x00,    0x03,0x45,0x00,    0x03,0x46,0x00,    0x03,0x47,0x00,
    0x03,0x48,0x00,    0x03,0x49,0x00,    0x03,0x4A,0x00,    0x03,0x4B,0x00,
    0x03,0x4C,0x00,    0x03,0x4D,0x00,    0x03,0x4E,0x00,    0x03,0x4F,0x00,
    0x03,0x50,0x00,    0x03,0x51,0x00,    0x03,0x52,0x00,    0x03,0x53,0x00,
    0x03,0x54,0x00,    0x03,0x55,0x00,    0x03,0x56,0x00,    0x03,0x57,0x00,
    0x03,0x58,0x00,    0x03,0x59,0x00,    0x03,0x5A,0x00,    0x03,0x5B,0x00,
    0x03,0x5C,0x00,    0x03,0x5D,0x00,    0x03,0x5E,0x00,    0x03,0x5F,0x00,
    0x03,0x60,0x00,    0x03,0x61,0x00,    0x03,0x62,0x00,

    0x04,0x87,0x01,

    0x05,0x02,0x01,    0x05,0x08,0x14,    0x05,0x09,0x23,    0x05,0x0A,0x0D,
    0x05,0x0B,0x0C,    0x05,0x0C,0x03,    0x05,0x0D,0x3F,    0x05,0x0E,0x18,
    0x05,0x0F,0x2D,    0x05,0x10,0x09,    0x05,0x11,0x08,    0x05,0x12,0x03,
    0x05,0x13,0x3F,    0x05,0x15,0x00,    0x05,0x16,0x00,    0x05,0x17,0x00,
    0x05,0x18,0x00,    0x05,0x19,0x70,    0x05,0x1A,0x03,    0x05,0x1B,0x00,
    0x05,0x1C,0x00,    0x05,0x1D,0x00,    0x05,0x1E,0x00,    0x05,0x1F,0x80,
    0x05,0x21,0x21,    0x05,0x2A,0x01,    0x05,0x2B,0x01,    0x05,0x2C,0x0F,
    0x05,0x2D,0x03,    0x05,0x2E,0x19,    0x05,0x2F,0x19,    0x05,0x31,0x00,
    0x05,0x32,0x10,    0x05,0x33,0x04,    0x05,0x34,0x00,    0x05,0x36,0x08,
    0x05,0x37,0x00,    0x05,0x38,0x00,    0x05,0x39,0x00,

    0x09,0x0E,0x02,    0x09,0x43,0x01,    0x09,0x49,0x0F,    0x09,0x4A,0x0F,

    0x0A,0x02,0x00,    0x0A,0x03,0x01,    0x0A,0x04,0x01,    0x0A,0x05,0x01,

    0x0B,0x44,0x2F,    0x0B,0x46,0x00,    0x0B,0x47,0x00,    0x0B,0x48,0x00,
    0x0B,0x4A,0x1E,

    0x05,0x14,0x01
  ],
 "390MHz": [
    0x00,0x06,0x00,    0x00,0x07,0x00,    0x00,0x08,0x00,    0x00,0x0B,0x68,    0x00,0x16,0x02,    0x00,0x17,0xDC,    0x00,0x18,0xB3,    0x00,0x19,0xDD,
    0x00,0x1A,0xDF,    0x00,0x2B,0x02,    0x00,0x2C,0x0C,    0x00,0x2D,0x50,    0x00,0x2E,0x00,    0x00,0x2F,0x00,    0x00,0x30,0x00,    0x00,0x31,0x00,
    0x00,0x32,0x39,    0x00,0x33,0x00,    0x00,0x34,0x39,    0x00,0x35,0x00,    0x00,0x36,0x00,    0x00,0x37,0x00,    0x00,0x38,0x00,    0x00,0x39,0x00,
    0x00,0x3A,0x39,    0x00,0x3B,0x00,    0x00,0x3C,0x39,    0x00,0x3D,0x00,    0x00,0x3F,0x44,    0x00,0x40,0x04,    0x00,0x41,0x00,    0x00,0x42,0x00,
    0x00,0x43,0x0E,    0x00,0x44,0x0E,    0x00,0x45,0x0C,    0x00,0x46,0x00,    0x00,0x47,0x00,    0x00,0x48,0x32,    0x00,0x49,0x00,    0x00,0x4A,0x00,
    0x00,0x4B,0x00,    0x00,0x4C,0x32,    0x00,0x4D,0x00,    0x00,0x4E,0x00,    0x00,0x4F,0x05,    0x00,0x50,0x07,    0x00,0x51,0x00,    0x00,0x52,0x00,
    0x00,0x53,0x03,    0x00,0x54,0x00,    0x00,0x55,0x00,    0x00,0x56,0x00,    0x00,0x57,0x03,    0x00,0x58,0x00,    0x00,0x59,0x10,    0x00,0x5A,0x00,
    0x00,0x5B,0x00,    0x00,0x5C,0x00,    0x00,0x5D,0x00,    0x00,0x5E,0x00,    0x00,0x5F,0x00,    0x00,0x60,0x00,    0x00,0x61,0x00,    0x00,0x62,0x55,
    0x00,0x63,0x55,    0x00,0x64,0xD0,    0x00,0x65,0x00,    0x00,0x66,0x00,    0x00,0x67,0x00,    0x00,0x68,0x00,    0x00,0x69,0x00,    0x00,0x92,0x02,
    0x00,0x93,0xA0,    0x00,0x95,0x00,    0x00,0x96,0x80,    0x00,0x98,0x60,    0x00,0x9A,0x02,    0x00,0x9B,0x60,    0x00,0x9D,0x08,    0x00,0x9E,0x40,
    0x00,0xA0,0x20,    0x00,0xA2,0x00,    0x00,0xA9,0xB2,    0x00,0xAA,0x61,    0x00,0xAB,0x00,    0x00,0xAC,0x00,    0x00,0xE5,0x00,    0x00,0xEA,0x0A,
    0x00,0xEB,0x60,    0x00,0xEC,0x00,    0x00,0xED,0x00,    0x01,0x02,0x01,    0x01,0x08,0x02,    0x01,0x09,0x09,    0x01,0x0A,0x3E,    0x01,0x0B,0x18,
    0x01,0x0D,0x02,    0x01,0x0E,0x09,    0x01,0x0F,0x3E,    0x01,0x10,0x18,    0x01,0x12,0x02,    0x01,0x13,0x09,    0x01,0x14,0x3E,    0x01,0x15,0x18,
    0x01,0x17,0x02,    0x01,0x18,0x09,    0x01,0x19,0x3E,    0x01,0x1A,0x18,    0x01,0x1C,0x02,    0x01,0x1D,0x09,    0x01,0x1E,0x3E,    0x01,0x1F,0x18,
    0x01,0x21,0x02,    0x01,0x22,0x09,    0x01,0x23,0x3E,    0x01,0x24,0x18,    0x01,0x26,0x02,    0x01,0x27,0x09,    0x01,0x28,0x3E,    0x01,0x29,0x18,
    0x01,0x2B,0x02,    0x01,0x2C,0x09,    0x01,0x2D,0x3E,    0x01,0x2E,0x18,    0x01,0x30,0x02,    0x01,0x31,0x09,    0x01,0x32,0x3E,    0x01,0x33,0x18,
    0x01,0x3A,0x02,    0x01,0x3B,0x09,    0x01,0x3C,0x3E,    0x01,0x3D,0x18,    0x01,0x3F,0x00,    0x01,0x40,0x08,    0x01,0x41,0x40,    0x01,0x42,0xFF,
    0x02,0x06,0x00,    0x02,0x08,0x00,    0x02,0x09,0x00,    0x02,0x0A,0x00,    0x02,0x0B,0x00,    0x02,0x0C,0x00,    0x02,0x0D,0x00,    0x02,0x0E,0x00,
    0x02,0x0F,0x00,    0x02,0x10,0x00,    0x02,0x11,0x00,    0x02,0x12,0x00,    0x02,0x13,0x00,    0x02,0x14,0x00,    0x02,0x15,0x00,    0x02,0x16,0x00,
    0x02,0x17,0x00,    0x02,0x18,0x00,    0x02,0x19,0x00,    0x02,0x1A,0x00,    0x02,0x1B,0x00,    0x02,0x1C,0x4F,    0x02,0x1D,0x00,    0x02,0x1E,0x00,
    0x02,0x1F,0x00,    0x02,0x20,0x00,    0x02,0x21,0x00,    0x02,0x22,0x01,    0x02,0x23,0x00,    0x02,0x24,0x00,    0x02,0x25,0x00,    0x02,0x26,0x4F,
    0x02,0x27,0x00,    0x02,0x28,0x00,    0x02,0x29,0x00,    0x02,0x2A,0x00,    0x02,0x2B,0x00,    0x02,0x2C,0x01,    0x02,0x2D,0x00,    0x02,0x2E,0x00,
    0x02,0x2F,0x00,    0x02,0x31,0x0B,    0x02,0x32,0x0B,    0x02,0x33,0x0B,    0x02,0x34,0x0B,    0x02,0x35,0x00,    0x02,0x36,0x00,    0x02,0x37,0x00,
    0x02,0x38,0x7C,    0x02,0x39,0x92,    0x02,0x3A,0x00,    0x02,0x3B,0x00,    0x02,0x3C,0x00,    0x02,0x3D,0x00,    0x02,0x3E,0x80,    0x02,0x4A,0x01,
    0x02,0x4B,0x00,    0x02,0x4C,0x00,    0x02,0x4D,0x01,    0x02,0x4E,0x00,    0x02,0x4F,0x00,    0x02,0x50,0x01,    0x02,0x51,0x00,    0x02,0x52,0x00,
    0x02,0x53,0x01,    0x02,0x54,0x00,    0x02,0x55,0x00,    0x02,0x56,0x01,    0x02,0x57,0x00,    0x02,0x58,0x00,    0x02,0x59,0x01,    0x02,0x5A,0x00,
    0x02,0x5B,0x00,    0x02,0x5C,0x01,    0x02,0x5D,0x00,    0x02,0x5E,0x00,    0x02,0x5F,0x01,    0x02,0x60,0x00,    0x02,0x61,0x00,    0x02,0x62,0x01,
    0x02,0x63,0x00,    0x02,0x64,0x00,    0x02,0x68,0x04,    0x02,0x69,0x00,    0x02,0x6A,0x00,    0x02,0x6B,0x00,    0x02,0x6C,0x00,    0x02,0x6D,0x00,
    0x02,0x6E,0x00,    0x02,0x6F,0x00,    0x02,0x70,0x00,    0x02,0x71,0x00,    0x02,0x72,0x00,    0x02,0x8A,0x00,    0x02,0x8B,0x00,    0x02,0x8C,0x00,
    0x02,0x8D,0x00,    0x02,0x8E,0x00,    0x02,0x8F,0x00,    0x02,0x90,0x00,    0x02,0x91,0x00,    0x02,0x94,0xB0,    0x02,0x96,0x02,    0x02,0x97,0x02,
    0x02,0x99,0x02,    0x02,0x9D,0xFA,    0x02,0x9E,0x01,    0x02,0x9F,0x00,    0x02,0xA9,0xCC,    0x02,0xAA,0x04,    0x02,0xAB,0x00,    0x02,0xB7,0xFF,
    0x03,0x02,0x00,    0x03,0x03,0x00,    0x03,0x04,0x00,    0x03,0x05,0x80,    0x03,0x06,0x04,    0x03,0x07,0x00,    0x03,0x08,0x00,    0x03,0x09,0x00,
    0x03,0x0A,0x00,    0x03,0x0B,0x80,    0x03,0x0C,0x00,    0x03,0x0D,0x00,    0x03,0x0E,0x00,    0x03,0x0F,0x00,    0x03,0x10,0x00,    0x03,0x11,0x00,
    0x03,0x12,0x00,    0x03,0x13,0x00,    0x03,0x14,0x00,    0x03,0x15,0x00,    0x03,0x16,0x00,    0x03,0x17,0x00,    0x03,0x18,0x00,    0x03,0x19,0x00,
    0x03,0x1A,0x00,    0x03,0x1B,0x00,    0x03,0x1C,0x00,    0x03,0x1D,0x00,    0x03,0x1E,0x00,    0x03,0x1F,0x00,    0x03,0x20,0x00,    0x03,0x21,0x00,
    0x03,0x22,0x00,    0x03,0x23,0x00,    0x03,0x24,0x00,    0x03,0x25,0x00,    0x03,0x26,0x00,    0x03,0x27,0x00,    0x03,0x28,0x00,    0x03,0x29,0x00,
    0x03,0x2A,0x00,    0x03,0x2B,0x00,    0x03,0x2C,0x00,    0x03,0x2D,0x00,    0x03,0x2E,0x00,    0x03,0x2F,0x00,    0x03,0x30,0x00,    0x03,0x31,0x00,
    0x03,0x32,0x00,    0x03,0x33,0x00,    0x03,0x34,0x00,    0x03,0x35,0x00,    0x03,0x36,0x00,    0x03,0x37,0x00,    0x03,0x38,0x00,    0x03,0x39,0x1F,
    0x03,0x3B,0x00,    0x03,0x3C,0x00,    0x03,0x3D,0x00,    0x03,0x3E,0x00,    0x03,0x3F,0x00,    0x03,0x40,0x00,    0x03,0x41,0x00,    0x03,0x42,0x00,
    0x03,0x43,0x00,    0x03,0x44,0x00,    0x03,0x45,0x00,    0x03,0x46,0x00,    0x03,0x47,0x00,    0x03,0x48,0x00,    0x03,0x49,0x00,    0x03,0x4A,0x00,
    0x03,0x4B,0x00,    0x03,0x4C,0x00,    0x03,0x4D,0x00,    0x03,0x4E,0x00,    0x03,0x4F,0x00,    0x03,0x50,0x00,    0x03,0x51,0x00,    0x03,0x52,0x00,
    0x03,0x53,0x00,    0x03,0x54,0x00,    0x03,0x55,0x00,    0x03,0x56,0x00,    0x03,0x57,0x00,    0x03,0x58,0x00,    0x03,0x59,0x00,    0x03,0x5A,0x00,
    0x03,0x5B,0x00,    0x03,0x5C,0x00,    0x03,0x5D,0x00,    0x03,0x5E,0x00,    0x03,0x5F,0x00,    0x03,0x60,0x00,    0x03,0x61,0x00,    0x03,0x62,0x00,
    0x04,0x87,0x05,    0x05,0x08,0x10,    0x05,0x09,0x1F,    0x05,0x0A,0x0C,    0x05,0x0B,0x0B,    0x05,0x0C,0x3F,    0x05,0x0D,0x3F,    0x05,0x0E,0x13,
    0x05,0x0F,0x27,    0x05,0x10,0x09,    0x05,0x11,0x08,    0x05,0x12,0x3F,    0x05,0x13,0x3F,    0x05,0x15,0x00,    0x05,0x16,0x00,    0x05,0x17,0x00,
    0x05,0x18,0x00,    0x05,0x19,0xC7,    0x05,0x1A,0x02,    0x05,0x1B,0x00,    0x05,0x1C,0x00,    0x05,0x1D,0x00,    0x05,0x1E,0x00,    0x05,0x1F,0x80,
    0x05,0x21,0x2B,    0x05,0x2A,0x05,    0x05,0x2B,0x01,    0x05,0x2C,0x87,    0x05,0x2D,0x03,    0x05,0x2E,0x19,    0x05,0x2F,0x19,    0x05,0x31,0x00,
    0x05,0x32,0x4B,    0x05,0x33,0x03,    0x05,0x34,0x00,    0x05,0x35,0x00,    0x05,0x36,0x00,    0x05,0x37,0x00,    0x05,0x38,0x00,    0x05,0x39,0x00,
    0x05,0x3A,0x02,    0x05,0x3B,0x03,    0x05,0x3C,0x00,    0x05,0x3D,0x11,    0x05,0x3E,0x06,    0x05,0x89,0x0D,    0x05,0x8A,0x00,    0x05,0x9B,0xF8,
    0x05,0x9D,0x10,    0x05,0x9E,0x21,    0x05,0x9F,0x0C,    0x05,0xA0,0x0B,    0x05,0xA1,0x3F,    0x05,0xA2,0x3F,    0x05,0xA6,0x03,    0x08,0x02,0x35,
    0x08,0x03,0x05,    0x08,0x04,0x00,    0x08,0x05,0x00,    0x08,0x06,0x00,    0x08,0x07,0x00,    0x08,0x08,0x00,    0x08,0x09,0x00,    0x08,0x0A,0x00,
    0x08,0x0B,0x00,    0x08,0x0C,0x00,    0x08,0x0D,0x00,    0x08,0x0E,0x00,    0x08,0x0F,0x00,    0x08,0x10,0x00,    0x08,0x11,0x00,    0x08,0x12,0x00,
    0x08,0x13,0x00,    0x08,0x14,0x00,    0x08,0x15,0x00,    0x08,0x16,0x00,    0x08,0x17,0x00,    0x08,0x18,0x00,    0x08,0x19,0x00,    0x08,0x1A,0x00,
    0x08,0x1B,0x00,    0x08,0x1C,0x00,    0x08,0x1D,0x00,    0x08,0x1E,0x00,    0x08,0x1F,0x00,    0x08,0x20,0x00,    0x08,0x21,0x00,    0x08,0x22,0x00,
    0x08,0x23,0x00,    0x08,0x24,0x00,    0x08,0x25,0x00,    0x08,0x26,0x00,    0x08,0x27,0x00,    0x08,0x28,0x00,    0x08,0x29,0x00,    0x08,0x2A,0x00,
    0x08,0x2B,0x00,    0x08,0x2C,0x00,    0x08,0x2D,0x00,    0x08,0x2E,0x00,    0x08,0x2F,0x00,    0x08,0x30,0x00,    0x08,0x31,0x00,    0x08,0x32,0x00,
    0x08,0x33,0x00,    0x08,0x34,0x00,    0x08,0x35,0x00,    0x08,0x36,0x00,    0x08,0x37,0x00,    0x08,0x38,0x00,    0x08,0x39,0x00,    0x08,0x3A,0x00,
    0x08,0x3B,0x00,    0x08,0x3C,0x00,    0x08,0x3D,0x00,    0x08,0x3E,0x00,    0x08,0x3F,0x00,    0x08,0x40,0x00,    0x08,0x41,0x00,    0x08,0x42,0x00,
    0x08,0x43,0x00,    0x08,0x44,0x00,    0x08,0x45,0x00,    0x08,0x46,0x00,    0x08,0x47,0x00,    0x08,0x48,0x00,    0x08,0x49,0x00,    0x08,0x4A,0x00,
    0x08,0x4B,0x00,    0x08,0x4C,0x00,    0x08,0x4D,0x00,    0x08,0x4E,0x00,    0x08,0x4F,0x00,    0x08,0x50,0x00,    0x08,0x51,0x00,    0x08,0x52,0x00,
    0x08,0x53,0x00,    0x08,0x54,0x00,    0x08,0x55,0x00,    0x08,0x56,0x00,    0x08,0x57,0x00,    0x08,0x58,0x00,    0x08,0x59,0x00,    0x08,0x5A,0x00,
    0x08,0x5B,0x00,    0x08,0x5C,0x00,    0x08,0x5D,0x00,    0x08,0x5E,0x00,    0x08,0x5F,0x00,    0x08,0x60,0x00,    0x08,0x61,0x00,    0x09,0x0E,0x02,
    0x09,0x43,0x01,    0x09,0x49,0x0C,    0x09,0x4A,0x0C,    0x09,0x4E,0x49,    0x09,0x4F,0x02,    0x09,0x5E,0x00,    0x0A,0x02,0x00,    0x0A,0x03,0x01,
    0x0A,0x04,0x01,    0x0A,0x05,0x01,    0x0A,0x14,0x08,    0x0A,0x1A,0x00,    0x0A,0x20,0x00,    0x0A,0x26,0x00,    0x0A,0x2C,0x00,    0x0B,0x44,0x2F,
    0x0B,0x46,0x00,    0x0B,0x47,0x03,    0x0B,0x48,0x03,    0x0B,0x4A,0x1E,    0x0B,0x57,0x0E,    0x0B,0x58,0x01
 ]
}
